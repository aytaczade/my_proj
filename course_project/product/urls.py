from django.urls import path,include

from core.views import contact
from .views import ProductListView, products_by_category, product_list, product_detail


urlpatterns = [
    path('products/categories/<slug:category_slug>', products_by_category, name='products_by_category'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<slug:product_slug>', product_detail, name='products_detail'),
    path('contact', contact, name='contact'),
    
]
