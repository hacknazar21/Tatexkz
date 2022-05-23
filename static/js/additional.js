
const promoCheckboxInput = document.querySelector('#promo')

if (promoCheckboxInput) {
    promoCheckboxInput.addEventListener('click', (event) => {
        
        inputPromo = document.querySelector('input[name="promo"]')
        
        if(promoCheckboxInput.checked){
        
        inputPromo.removeAttribute('hidden')
        inputPromo.parentElement.style.cssText = ""
        inputPromo.focus()}
        else {
            inputPromo.setAttribute('hidden', "")
            inputPromo.parentElement.style.cssText = "margin: 0; padding:0;"
        }
    })
}

