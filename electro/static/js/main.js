const linkProductBtn = document.getElementById("link-product-page")

function gotoProduct(){
    document.location.href = "../html/product.html"
}

linkProductBtn.addEventListener("click", gotoProduct)