const inputs = document.querySelectorAll('[data-inputcity]')
const cities = []

async function getCities() {
    const response = await fetch('/order/getcountries/cities')
    const data = await response.json()
    return data
}

if (inputs.length != 0) {
    getCities().then(data => {
        for (const key in data) {
            for (const city of data[key]) {
                cities.push(city)
            }
        }
    })
    for (const input of inputs) {
        const listHTML = document.createElement('ul');
        input.insertAdjacentElement('afterend', listHTML)
        input.addEventListener('input', () => {
            const currentVal = input.value.trim().toLowerCase();
            let filteredCities = ''
            listHTML.classList.add('searchHidden');
            for (const city of cities) {
                if (currentVal == '') {
                    listHTML.classList.remove('searchHidden');
                    break
                }
                const currentCity = city.trim().toLowerCase()
                if (currentCity.includes(currentVal)) filteredCities += `<li class="search-item">${city}</li>`
            }
            listHTML.innerHTML = filteredCities

            for (const li of document.querySelectorAll('.search-item')) {
                li.addEventListener('click', () => {
                    input.value = li.innerHTML
                    listHTML.classList.remove('searchHidden');
                    listHTML.innerHTML = ''
                })
            }
        })
    }
}