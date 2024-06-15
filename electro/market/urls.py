from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePageView.as_view(), name="home-page"),
    path('products/<int:id>/', views.ProductPageView.as_view(), name="product"),
]
