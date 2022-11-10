from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.getDetailMe),
    path('contact-messages/', views.getContactMessage),
    path('coding-skill-list/', views.getCodingSkillsList),
    path('frameworks-learned-list/', views.getFrameworksList),
    path('portfolio-list/', views.getPortfolioList),
    path('certificate-list/', views.getCertificateList),
    path('testimony-list/', views.getTestimonyList),
]