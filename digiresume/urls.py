from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('blog-detail/<int:pk>/', views.blog_detail, name="blog-detail"),
    path('contact/', views.contact, name="contact"),
    path('save_client/', views.save_clients, name="save"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio-detail/<int-pk/',views.portfolio_detail, name="portfolio-detail"),
]