from django.urls import path
from .views import index, contact, search, about

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('search', search, name='search'),
     path('about', about, name='about')
    
]