from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'user_office'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profileCustomer/', views.profile, name='profile_customer'),
    path('profileSeller/', views.profile, name='profile_seller'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)