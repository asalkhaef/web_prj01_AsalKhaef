from django.shortcuts import render

# Create your views here.


def showHome(request):
    return render(request, "index.html")


def showProduct(request):
    return render(request, "product.html")
