let cupcakesClicked = document.querySelector('.cupcakes-clicked');

function incrementCupcakes() {
    cupcakesClicked.innerHTML = parseFloat(cupcakesClicked.innerHTML) + 1;
}