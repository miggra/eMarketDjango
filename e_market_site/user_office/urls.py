from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'user_office'
urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('profile/add_new_product', views.add_new_product, name='add_new_product'),
    path('profile/edit_product/<int:pk>', views.UpdateProductView.as_view(), name='update_product'),
    path('profile/delete_product/<int:pk>', views.DeleteProductView.as_view(), name='delete_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)