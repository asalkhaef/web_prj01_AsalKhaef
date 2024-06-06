const loginModal = document.getElementById("modal-login")
const registerModal = document.getElementById("modal-register")
const overlayAuth = document.getElementById("modal-overlay__auth")
const overlayCart = document.getElementById("modal-overlay__cart")
const loginBtn = document.getElementById("login-button-mainpage")
const modalCards = document.getElementsByClassName("modal-card")

const modalCloseBtn = document.getElementsByClassName("modal-close-btn")[0]

const registerBtn = document.getElementById("register-btn")

const cartIcon = document.getElementById("cart-icon")
const sideBar = document.getElementById("mini-cart-sidebar")
const checkoutBtn = document.getElementById("checkout-btn-id")

const trashIcons = document.getElementsByClassName("trash-icon")
const cartItemNum = document.getElementById("num-items")

const forgetBtn = document.getElementById("forget-btn-id")
const otpModal = document.getElementById("modal-otp")

const submitOtpBtn = document.getElementById("otp-submit-btn-id")
const successModal = document.getElementById("modal-successful-login")

const optBackBtn = document.getElementById("opt-back-btn")
const iphoneNum2 = document.getElementById("iphone-num")
const cartNumber2 = document.getElementsByClassName("number-of-cart")[0]


function showLoginModal(){
    loginModal.style.display = "block"
    overlayAuth.style.display = "flex"
}

loginBtn.addEventListener("click", showLoginModal)

function closeModalsAuth(){
    for (let item of modalCards) {
        item.style.display = "none"
    }
    overlayAuth.style.display = "none"
}

modalCloseBtn.addEventListener("click", closeModalsAuth)

function showRegisterModal(){
    registerModal.style.display = "block"
    loginModal.style.display = "none"
}

registerBtn.addEventListener("click", showRegisterModal)

function openSideBarCart(){
    overlayCart.style.display = "block"
    sideBar.style.display = "flex"
}

cartIcon.addEventListener("click", openSideBarCart)

function closeModalsCart(){
    for (let item of modalCards) {
        item.style.display = "none"
    }
    overlayCart.style.display = "none"
}

checkoutBtn.addEventListener("click", closeModalsCart)

for (let icon of trashIcons) {
    icon.addEventListener("click", (event) => {
        console.log('event.target :>> ', event.target.id);
        const productIndex = event.target.id.split("-")[3];
        let productId = `product-item-${productIndex}`
        document.getElementById(productId).remove()
        let currentNum = Number(cartItemNum.innerText)
        if(productId == "product-item-1")
            currentNum = currentNum - Number(iphoneNum2.innerText)
        else
            currentNum--
        cartItemNum.innerText = currentNum
        cartNumber2.innerText = currentNum

    })
}

function openOTP(){
    otpModal.style.display = "block"
    loginModal.style.display = "none"
}

forgetBtn.addEventListener("click", openOTP)

function openSuccess(){
    otpModal.style.display = "none"
    successModal.style.display = "flex"
}

submitOtpBtn.addEventListener("click", openSuccess)

function backToLogin(){
    successModal.style.display = "none"
    loginModal.style.display = "block"
    
}
optBackBtn.addEventListener("click", backToLogin)






