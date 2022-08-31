from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render


# Create your views here.

menu_items = [{'title': "Главная", 'url_name': 'shop:index'},
            {'title': "Личный кабинет", 'url_name': 'user_office:profile'},
            {'title': "Корзина", 'url_name': 'shop:cart'}]

def index(request):
    """
    Home page
    """
    template = loader.get_template('shop/index.html')
    context = {
        'title' : 'eMarke',
        'menu_items' : menu_items
    }
    return HttpResponse(template.render(context, request))

def cart(request):
    raise Http404("Page not found")