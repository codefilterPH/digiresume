from django.urls import path
from .import views

urlpatterns = [
    path('weather/', views.index, name="index"),
    path('weather/selected/<slug:pk>/', views.click, name="click"),
]