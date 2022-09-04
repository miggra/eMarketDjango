
import pdb
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from shop.menu import Menu

from shop.models import Product

from .forms import AddProductForm

def is_seller(user):
    return user.groups.filter(name='Sellers').exists()

def is_customer(user):
    return user.groups.filter(name='Customers').exists()

def get_seller_context(user):
    seller_products = user.seller.product_set.all()
    context = {
        'user': user,
        'shop_name': user.seller.shop_name,
        'seller_products' : seller_products 
    }
    return context

# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        return redirect(reverse('accounts:login'))
    user = request.user
    context = {        
        'menu': Menu(request)
    }
    if is_seller(user):
        context = dict(context, **get_seller_context(user))
        return render(request, 'user_office/profile_seller.html', context)
    else:    
        return render(request, 'user_office/profile_customer.html', context)


def add_new_product(request):
    user = request.user
    if request.method == 'POST':
        add_product_form = AddProductForm(request.POST, request.FILES) 
      
        if not add_product_form.is_valid():
            return HttpResponse('Form is not valid')

        new_product = add_product_form.save(commit=False)
        new_product.seller = user.seller
        new_product.save()        
        add_product_form.save_m2m()
        return redirect(reverse('user_office:profile'))
    else:
        add_product_form = AddProductForm()        
        args = {
            'add_product_form': add_product_form
            }
        context = dict(**get_seller_context(user), **args) 
        
        return render(request, 'user_office/add_new_product.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'user_office/product_details.html'

class UpdateProductView(UpdateView):
    model = Product
    template_name = 'user_office/update_product.html'
    fields = (
            'name',
            'category',
            'description',
            'price',
            'main_image',
            'count'
        )

    def get_success_url(self) -> str:
        return reverse('user_office:profile')
        

class DeleteProductView(DeleteView):
    model = Product
    template_name = 'user_office/deleteconfirmation.html'

    def get_success_url(self) -> str:
        return reverse('user_office:profile')