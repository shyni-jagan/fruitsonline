from django.urls import path
from .import views
urlpatterns=[
    path('',views.home),
    path('about/',views.about,name='about'),
    path('products/',views.products,name='products'),
    path('login/',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('contact/',views.contact,name='contact')




]