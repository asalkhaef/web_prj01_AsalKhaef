const productTabContent = document.getElementsByClassName("option-content")
const productTabBtns = document.getElementsByClassName("description-part-top-child-options")
const descriptionBtn = document.getElementById("description-btn")
const additionalInfoBtn = document.getElementById("additional-info-btn")
const reviewBtn = document.getElementById("review-btn")
const blueLine = document.getElementsByClassName("data-divider-blue-line")[0]

const productPrice = document.getElementsByClassName("product-detail-price")[0]
const productColor = document.getElementsByClassName("color-option")
const productBasePrice = document.querySelector(".product-detail-price")

const cartNumber = document.getElementsByClassName("number-of-cart")[0]
const cartBtn = document.getElementById("add-to-cart-button-id")

const cartItemNum2 = document.getElementById("num-items")
const iphoneNum = document.getElementById("iphone-num")

console.log(productBasePrice)

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

// change price based on color!
for (let item of productColor) {
    item.addEventListener("click", (event) => {
        const priceToSet = Number(event.target.dataset.price) + Number(productBasePrice.dataset.basePrice)
        productPrice.innerHTML = priceToSet.toFixed(2)
    })
}

function addCart(){
    let currentCartNumber = Number(cartNumber.innerText)
    currentCartNumber = currentCartNumber + 1
    cartNumber.innerText = currentCartNumber
    cartItemNum2.innerText = currentCartNumber
    iphoneNum.innerText = currentCartNumber - 1
}

cartBtn.addEventListener("click", addCart)

const linkMainBtn = document.getElementsByClassName("logo-text")[0]

function gotoMainPage(){
    document.location.href = "../html/index.html"
}

linkMainBtn.addEventListener("click", gotoMainPage)
