from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    # post views
    #path('login/', views.user_login, name='login'),
    path('login/',
         views.ExtendedLoginView.as_view(),
         name='login'),
    path('logout/',
        auth_views.LogoutView.as_view(
            next_page = 'shop:index'),
        name='logout'),

    path('register/',
        views.register,
        name='register'),

    path('register/seller/',
        views.register_seller,
        name='register_seller'),
    
    path('register/customer/',
        views.register_customer,
        name='register_customer'),
]