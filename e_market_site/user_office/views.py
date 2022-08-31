
import pdb
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect

def is_seller(user):
    return user.groups.filter(name='Sellers').exists()

def is_customer(user):
    return user.groups.filter(name='Customers').exists()

# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        return redirect(reverse('accounts:login'))
    user = request.user
    if is_seller(user):
        seller_products = user.seller.product_set.all()
        context = {
            'user': user,
            'shop_name': user.seller.shop_name,
            'seller_products' : seller_products 
        }
        return render(request, 'user_office/profile_seller.html', context)
    else:    
        return render(request, 'user_office/profile_customer.html')