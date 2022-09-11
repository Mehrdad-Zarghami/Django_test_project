from django.urls import path
from . import views

urlpatterns = [
    path('', views.e_shop, name='home_page'),
    path('about/', views.about, name='about_page'),
    path('contact_us/', views.contact_us, name='contact_us_page')
]
