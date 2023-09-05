from django.contrib import admin
from .models import OrderItem, MainOrder, WishList

admin.site.register(OrderItem)
admin.site.register(MainOrder)
admin.site.register(WishList)