const productTabContent = document.getElementsByClassName("option-content")
const productTabBtns = document.getElementsByClassName("description-part-top-child-options")
const descriptionBtn = document.getElementById("description-btn")
const additionalInfoBtn = document.getElementById("additional-info-btn")
const reviewBtn = document.getElementById("review-btn")
const blueLine = document.getElementsByClassName("data-divider-blue-line")[0]

const productPrice = document.getElementsByClassName("product-detail-price")[0]
const productColor = document.getElementsByClassName("color-option")

console.log(productPrice.innerHTML)



function openProductDescription(){
    for (let item of productTabContent) {
        item.style.display = "none"
    }

    productTabContent[0].style.display = "block"

    blueLine.style.left = "0px"
    blueLine.style.width = "105px"

    for (let item of productTabBtns) {
        item.classList.remove("description-blue")
    }

    productTabBtns[0].classList.add("description-blue")

}

descriptionBtn.addEventListener("click", openProductDescription)


function openProductAdditionalInfo(){
    for (let item of productTabContent) {
        item.style.display = "none"
    }

    productTabContent[2].style.display = "flex"

    blueLine.style.left = "138px"
    blueLine.style.width = "176px"

    for (let item of productTabBtns) {
        item.classList.remove("description-blue")
    }

    productTabBtns[1].classList.add("description-blue")
}

additionalInfoBtn.addEventListener("click", openProductAdditionalInfo)


function openProductReview(){
    for (let item of productTabContent) {
        item.style.display = "none"
    }

    productTabContent[1].style.display = "flex"

    blueLine.style.left = "329px"
    blueLine.style.width = "100px"

    for (let item of productTabBtns) {
        item.classList.remove("description-blue")
    }

    productTabBtns[2].classList.add("description-blue")
}

reviewBtn.addEventListener("click", openProductReview)

for (let item of productColor) {
    item.addEventListener("click", (event) => {
        if(event.target.classList[1] == "color1")
            productPrice.innerHTML = "$1999.00"
        else if (event.target.classList[1] == "color2")
            productPrice.innerHTML = "$1800.00"
        else if (event.target.classList[1] == "color3")
            productPrice.innerHTML = "$1700.00"
        else if (event.target.classList[1] == "color4")
            productPrice.innerHTML = "$1600.00"
    })
}
