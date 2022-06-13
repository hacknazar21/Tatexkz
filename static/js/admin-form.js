window.onload = () => {
    const minRange = document.querySelector('[name="shipmentDate"]')
    const maxRange = document.querySelector('[name="shipmentDateFuture"]')
    const statusField = document.querySelector('.field-status')
    if(minRange && maxRange){
        const minRangeHidden = document.createElement('input')
        const maxRangeHidden = document.createElement('input')

        minRangeHidden.name = minRange.name
        maxRangeHidden.name = maxRange.name
        minRangeHidden.id = minRange.id
        maxRangeHidden.id = maxRange.id
        minRangeHidden.type = "hidden"
        maxRangeHidden.type = "hidden"
        minRange.name = ""
        maxRange.name = ""
        minRange.id = ""
        maxRange.id = ""
        minRange.insertAdjacentElement('afterend', minRangeHidden)
        maxRange.insertAdjacentElement('afterend', maxRangeHidden)

        minRange.type = 'range'
        maxRange.type = 'range'
        minRange.style.minWidth = '46em'
        maxRange.style.minWidth = '46em'

        
        setMinMaxTime(minRange, maxRange, minRangeHidden, maxRangeHidden)
    }
    updateStatus(statusField)
    setInterval(updateStatus(statusField), 30000)
    const submitBtns = document.querySelectorAll('.dhl-button')
    submitBtns.forEach(submitBtn => {
        const img = document.createElement('img')
        const inputs = submitBtn.parentElement.querySelectorAll('input[type="hidden"]')
        img.src = '/static/img/load.svg'
        img.style.width = '32px';
        img.style.height = '1%';

        submitBtn.addEventListener('click', (event) => {
            event.preventDefault()
            submitBtn.innerHTML = 'Отправляется'
            submitBtn.disabled = "disabled"
            submitBtn.parentElement.insertAdjacentElement('beforeend', img)
            gotoDHL(inputs).then((resp) => {
                submitBtn.innerHTML = 'Отправлено'
                document.querySelector('img').remove()
                location.reload()
            })

        })
    });

    async function gotoDHL(inputs) {
        data = {}
        for (const input of inputs) {
            const key = input.name, val = input.value
            data[key] = val
        }
        let response = await fetch("/gotodhl/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=utf-8"
            },
            body: JSON.stringify(data)
        });
        return await response.json();
    }
}

function updateStatus() { 
    const tracks = document.querySelectorAll('.field-trackcode a')
    async function updateStatus(track) {
        data = {}
        data['trackcode'] = track
        let response = await fetch("/status/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=utf-8"
            },
            body: JSON.stringify(data)
        });
        return await response.json();
    }
    tracks.forEach(track => {
        const statusField = track.parentElement.closest('tr').querySelector('.field-status')
        if(track.innerText != '0000000000'){
            console.log(track.innerText)
            updateStatus(track.innerText).then((data)=>{
                statusField.innerText = data['Status'][0]
            })
        }
    });
    
}
function setMinMaxTime(minel, maxel, minhidden, maxhidden){
    const sendDate = document.querySelector('input[name="dataSend"]')
    const sendDateMass = sendDate.value.split('/')
    let nowTime = 0
    if(new Date(sendDateMass[2], sendDateMass[1], sendDateMass[0]) > new Date()){
        nowTime = 10*60
    }
    else{
        nowTime = new Date().getHours()*60 + new Date().getMinutes()
    }
    const maxTime = 18*60
    minel.setAttribute('step', fromMinMaxTimeToPercent(615))
    maxel.setAttribute('step', fromMinMaxTimeToPercent(615))
    const minLabel = document.createElement('p')
    const maxLabel = document.createElement('p')
    

    minLabel.innerText = document.querySelector(`input[name="initial-${minhidden.name}"]`).value
    maxLabel.innerText = document.querySelector(`input[name="initial-${maxhidden.name}"]`).value
    minhidden.value = document.querySelector(`input[name="initial-${minhidden.name}"]`).value
    maxhidden.value = document.querySelector(`input[name="initial-${maxhidden.name}"]`).value
    minel.value = fromMinMaxTimeToPercent(parseInt(minLabel.innerText.split(':')[0])*60+parseInt(minLabel.innerText.split(':')[1]))
    maxel.value = fromMinMaxTimeToPercent(parseInt(maxLabel.innerText.split(':')[0])*60+parseInt(maxLabel.innerText.split(':')[1]))
    minel.insertAdjacentElement('afterend', minLabel)
    maxel.insertAdjacentElement('afterend', maxLabel)
    
    minel.addEventListener('input', (event)=>{
        minLabel.innerText = fromMinutesToStr(minel.value)
        minhidden.value = fromMinutesToStr(minel.value)
    })
    maxel.addEventListener('input', (event)=>{
        maxLabel.innerText = fromMinutesToStr(maxel.value)
        maxhidden.value = fromMinutesToStr(maxel.value)
    })
    if(maxTime - nowTime < 60) {
        minel.setAttribute('min', nowTime)
        minel.setAttribute('max', maxTime)
        maxel.setAttribute('min', nowTime)
        maxel.setAttribute('max', maxTime)
        minel.value = nowTime
        maxel.value = maxTime
        minel.disabled = true
        maxel.disabled = true
    }
    else{
        minel.setAttribute('min', fromMinMaxTimeToPercent(nowTime))
        minel.setAttribute('max', fromMinMaxTimeToPercent(maxTime - 60))
        maxel.setAttribute('min', fromMinMaxTimeToPercent(nowTime + 75))
        maxel.setAttribute('max', fromMinMaxTimeToPercent(maxTime))
    }
    console.log(nowTime, maxTime)
}

function fromMinMaxTimeToPercent(time){
    while(time % 15){
        time++
    }
    return (time - 10*60)*100/(18*60 - 10*60)
}
function fromPercentToMinMaxTime(percent){
    return (percent * (18*60 - 10*60) / 100) + 10*60
}
function fromMinutesToStr(minutes){
    minutes = fromPercentToMinMaxTime(minutes)
    let minute = Math.round((minutes/60 - Math.floor(minutes/60))*60)
    let hour = Math.floor(minutes/60)
    if(minute == 60){
        minute = 0
        hour++
    }
    return `${hour}:${minute == 0 ? minute.toString() + '0': minute}:00`
}