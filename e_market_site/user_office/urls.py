from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'user_office'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/add_new_product', views.add_new_product, name='add_new_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)