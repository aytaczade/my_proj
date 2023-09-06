from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from product.models import Category, Product, Campaign
from about.models import About, Store
from django.db.models import Q
from django.contrib import messages
from .forms import ContactForm


def index(request):
    context = {
        'trandy_products': Product.objects.filter(is_trand=True)[:8],
        'just_arrived_products': Product.objects.all().order_by('-created_at')[:8],
        'campaigns': Campaign.objects.all()[:2],
    }
    return render(request, 'home/index.html', context)


def contact(request):
    stores = Store.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Müraciətiniz uğurla qeydə alındı, tezliklə sizinlə əlaqə saxlanılacaq')
            return redirect(reverse("contact"))

    context = {
        'stores': stores,
        'form': form,
    }
    return render(request, 'contact/index.html', context)


def search(request):
    query = request.GET.get('search')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'result_count': len(products),
        'query': query,
        'results': products
    }

    return render(request, 'product/search.html', context)


def about(request):
    about = About.objects.first()
    context = {
        'about': about,
    }
    return render(request, 'about/index.html', context)