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
        currentNum--
        cartItemNum.innerText = currentNum
    })
}





