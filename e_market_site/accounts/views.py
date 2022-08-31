import pdb
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group

from .models import Customer
from .forms import LoginForm, RegisterForm, SellerRegisterForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def register(request):
    return render(request, 'accounts/register.html')

def register_customer(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password1'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    new_customer = Customer(user=user)          
                    new_customer.save()          
                    return redirect(reverse('user_office:profile_customer'))
                else:
                    return HttpResponse('Disabled account')
    else:
        form = RegisterForm()
        args = {'form': form}
        return render(request, 'accounts/register_customer.html', context=args)

def register_seller(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)        
        seller_form = SellerRegisterForm(request.POST)
        if (not user_form.is_valid() 
            or not seller_form.is_valid()):
            return
        user_form.save()
        cd = user_form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password1'])
        if user is None or  not user.is_active:
            return
        login(request, user)    
        sellers = Group.objects.get(name='Sellers')
        sellers.user_set.add(user)

        new_seller = seller_form.save(commit=False)
        new_seller.user = request.user
        new_seller.save()
        seller_form.save_m2m()
        return redirect(reverse('user_office:profile_seller'))
    else:
        user_form = RegisterForm()
        seller_form = SellerRegisterForm()
        args = {
            'user_form': user_form,
            'seller_form': seller_form
            }
        return render(request, 'accounts/register_seller.html', context=args)
