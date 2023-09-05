from django.views import generic
from django.shortcuts import render
from .models import Category,Product
from .utils.helpers import get_values_from_choices
from .utils.options import *

def products_by_category(request,category_slug):
    category=Category.objects.get(slug=category_slug)
    context={
        'category':category,
    }
    return render(request, 'product/products_by_category.html', context)


def product_list(request):
    products=Product.objects.all()
    context={
        'products':products,
    }
    return render(request, 'product/product_list.html', context)

class ProductListView(generic.ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 8


def product_detail(request,product_slug):
    product=Product.objects.get(slug=product_slug)
    cat_ids = [obj.id for obj in product.category.all()]
    context={
        'product':product,
        'sizes':get_values_from_choices(SIZES),
        'colors':get_values_from_choices(COLORS),
                'related_products': Product.objects.filter(category__in=cat_ids).distinct()[:8],
    }
    return render(request, 'product/detail.html', context)