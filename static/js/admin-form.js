window.onload = () => {
    const inputs = document.querySelectorAll('input[type="hidden"]')
    const submitBtns = document.querySelectorAll('.dhl-button')
    submitBtns.forEach(submitBtn => {
        const img = document.createElement('img')
        img.src = '/static/img/load.svg'
        img.style.width = '32px';
        img.style.height = '1%';

        submitBtn.addEventListener('click', (event) => {
            event.preventDefault()
            submitBtn.innerHTML = 'Отправляется'
            submitBtn.disabled = "disabled"
            submitBtn.parentElement.insertAdjacentElement('beforeend', img)
            gotoDHL().then((resp) => {
                submitBtn.innerHTML = 'Отправлено'
                document.querySelector('img').remove()
            })

        })
    });

    async function gotoDHL() {
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

