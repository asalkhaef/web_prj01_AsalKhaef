const loginModal = document.getElementById("modal-login")
const registerModal = document.getElementById("modal-register")
const overlay = document.getElementById("modal-overlay")
const loginBtn = document.getElementById("login-button-mainpage")
const modalCards = document.getElementsByClassName("modal-card")

const modalCloseBtn = document.getElementsByClassName("modal-close-btn")[0]

const registerBtn = document.getElementById("register-btn")



function showLoginModal(){
    loginModal.style.display = "block"
    overlay.style.display = "flex"
}

loginBtn.addEventListener("click", showLoginModal)

function closeModals(){
    for (let item of modalCards) {
        item.style.display = "none"
    }
    overlay.style.display = "none"
}

modalCloseBtn.addEventListener("click", closeModals)

function showRegisterModal(){
    registerModal.style.display = "block"
    loginModal.style.display = "none"
}

registerBtn.addEventListener("click", showRegisterModal)








