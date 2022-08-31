from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import Product
from cart.forms import CartAddProductForm 
# Create your views here.

menu_items = [{'title': "Главная", 'url_name': 'shop:index'},
            {'title': "Личный кабинет", 'url_name': 'user_office:profile'},
            {'title': "Корзина", 'url_name': 'shop:cart'}]

def index(request):
    """
    Home page
    """
    template = loader.get_template('shop/index.html')
    products = Product.objects.order_by('-updated')[:10]
    cart_product_form = CartAddProductForm()
    context = {
        'title' : 'eMarke',
        'menu_items' : menu_items,
        'products': products,
        'cart_product_form': cart_product_form
    }
    return HttpResponse(template.render(context, request))

def cart(request):
    raise Http404("Page not found")