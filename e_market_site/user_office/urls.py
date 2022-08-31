from django.urls import path

from . import views

app_name = 'user_office'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profileCustomer/', views.profile, name='profile_customer'),
    path('profileSeller/', views.profile, name='profile_seller'),
]