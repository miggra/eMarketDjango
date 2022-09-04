from audioop import reverse
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import Product
from cart.forms import CartAddProductForm 
# Create your views here.

def index(request):
    """
    Home page
    """
    user = request.user
    if user.groups.filter(name='Sellers').exists():
        return render_home_page_for_seller(request)
    else:    
        return render_home_page_for_customer(request)

def render_home_page_for_customer(request):
    products = Product.objects.order_by('-updated')[:10]
    cart_product_form = CartAddProductForm()
    context = {
        'title' : 'eMarke',
        'products': products,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/home_customer.html', context) 

def render_home_page_for_seller(request):
    products = Product.objects.order_by('-updated')[:10]
    cart_product_form = CartAddProductForm()
    context = {
        'title' : 'eMarke',
        'products': products,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/home_customer.html', context)