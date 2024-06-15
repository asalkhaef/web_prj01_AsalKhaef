from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePageView.as_view(), name="home-page"),
    path('product/', views.HomePageView.as_view(), name="product"),
]
