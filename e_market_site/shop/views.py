import pdb
from turtle import pd
from .menu import Menu
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
    menu = Menu(request)  
    user = request.user
    if user.groups.filter(name='Sellers').exists():
        return render_home_page_for_seller(request, menu)
    else:   
        return render_home_page_for_customer(request, menu)

def render_home_page_for_customer(request, menu):
    products = Product.objects.order_by('-updated')[:10]
    cart_product_form = CartAddProductForm()
    context = {
        'menu' : menu,
        'products': products,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/home_customer.html', context) 

def render_home_page_for_seller(request, menu):
    context = {
        'menu' : menu
    }
    return render(request, 'shop/home_seller.html', context)