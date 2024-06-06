from django.urls import path
from . import views

urlpatterns = [
    path("Homepage/", views.showHome, name="home"),
    path("Product/", views.showProduct, name="product")
]
