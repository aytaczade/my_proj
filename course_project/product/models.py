from typing import Iterable, Optional
from django.db import models

from .utils.options import CURRENCIES, COLORS, SIZES

from order.models import WishList
from utils.current_request import get_current_request

class Category(models.Model):
    name = models.CharField(
        'ad', max_length=200
    )
    slug = models.SlugField(
        unique=True,
    )
    image = models.ImageField(
        upload_to='categories',
        null=True,
        blank=True,
    )
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.slug
    
    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'


class Product(models.Model):
    name = models.CharField(
        'ad', max_length=200
    )
    description = models.TextField(
        'təsviri'
    )
    price = models.DecimalField(
        'qiymət',
        decimal_places=2,
        max_digits=10
    )
    price_currency = models.CharField(
        max_length=50,
        choices=CURRENCIES, 
        default='AZN'
    )
    category = models.ManyToManyField(
        'product.Category', 
        related_name='products'
    )
    size = models.CharField(
        max_length=20,
        choices=SIZES
    )
    color = models.CharField(
        max_length=20,
        choices=COLORS
    )
    slug = models.SlugField(unique=True,)
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        )
    is_trand = models.BooleanField(default=False)
    has_discount = models.BooleanField(default=False)
    old_price = models.DecimalField(
        'əvvəlki qiymət',
        decimal_places=2,
        max_digits=10,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache_price = self.price

    def save(self):
        if self.cache_price and self.cache_price != self.price:
            if self.cache_price > self.price:
                self.has_discount = True 
            else:
                self.has_discount = False     
            self.old_price = self.cache_price
        return super().save()

    class Meta:
        verbose_name = 'Məhsul'
        verbose_name_plural = 'Məhsullar'

    @property
    def has_added_to_wish_list(self):
        request = get_current_request()
        wl = WishList.objects.filter(user=request.user).first()
        product = Product.objects.filter(id=self.id).first()
        if wl and product:
            if product in wl.product.all():
                return True 
        return False


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(
        'şəkil', 
        upload_to='products'
    )

    def __str__(self):
        return self.image.name.split("/")[1]

    class Meta:
        verbose_name = 'Məhsul şəkli'
        verbose_name_plural = 'Məhsullar şəkilləri'


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    percent = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kompaniya'
        verbose_name_plural = 'Kompaniyalar'