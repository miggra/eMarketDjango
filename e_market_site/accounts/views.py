from multiprocessing import context
import pdb
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group

from shop.menu import Menu

from .models import Customer
from .forms import LoginForm, RegisterForm, SellerRegisterForm
from django.contrib.auth.views import LoginView

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if not form.is_valid():
#             return HttpResponse('Invalid login')
#         cd = form.cleaned_data
#         user = authenticate(username=cd['username'], password=cd['password'])
#         if user is None:
#             return HttpResponse('User not exists')
#         if not user.is_active:
#             return HttpResponse('Disabled account')
#         login(request, user)
#         return HttpResponse('Authenticated successfully')
#     else:
#         form = LoginForm()
#     return render(request, 'accounts/login.html', {'form': form})


def register(request):
    
    return render(request, 'accounts/register.html', 
            {'menu' : Menu(request)})

def register_customer(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return HttpResponse('Form is not valid')
        form.save()
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password1'])
        if user is None:
            return HttpResponse('User not exists')
        if not user.is_active:
            return HttpResponse('Disabled account')
        login(request, user)
        customers = Group.objects.get(name='Customers')
        customers.user_set.add(user)
        new_customer = Customer(user=user)          
        new_customer.save()          
        return redirect(reverse('user_office:profile'))
    else:
        form = RegisterForm()
        args = {
            'menu' : Menu(request),
            'form': form}
        return render(request, 'accounts/register_customer.html', context=args)

def register_seller(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)        
        seller_form = SellerRegisterForm(request.POST)
        if (not user_form.is_valid() 
            or not seller_form.is_valid()):
            return HttpResponse('Form is not valid')
        user_form.save()
        cd = user_form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password1'])
        if user is None:
            return HttpResponse('User not exists')
        if not user.is_active:
            return HttpResponse('Disabled account')
        login(request, user)    
        sellers = Group.objects.get(name='Sellers')
        sellers.user_set.add(user)

        new_seller = seller_form.save(commit=False)
        new_seller.user = request.user
        new_seller.save()
        seller_form.save_m2m()
        return redirect(reverse('user_office:profile'))
    else:
        user_form = RegisterForm()
        seller_form = SellerRegisterForm()
        args = {            
            'menu' : Menu(request),
            'user_form': user_form,
            'seller_form': seller_form
            }
        return render(request, 'accounts/register_seller.html', context=args)

class ExtendedLoginView(LoginView):
    template_name='accounts/login.html'
    next_page = 'user_office:profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = {'menu' : Menu(self.request)}
        context.update(extra_context)
        return context