from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    # post views
    #path('login/', views.user_login, name='login'),
    path('login/',
         auth_views.LoginView.as_view(
            template_name='accounts/login.html',
            next_page = 'shop:index'),
         name='login'),
    path('logout/',
        auth_views.LogoutView.as_view(
            next_page = 'shop:index'),
        name='logout'),
    path('registerAsSeller/',
        views.register_seller,
        name='register_seller'),
    
    path('registerAsCustomer/',
        views.register_customer,
        name='register_customer'),
]