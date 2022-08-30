from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    phone = models.CharField("phone_number", max_length=12, blank=True)
    pass
class Seller(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    shop_name = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.shop_name}:{self.user.username}' 

    # def __str__(self):
    #     return ['self.shop_name']

class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = kwargs.get('user')
        if (user is not None):
            self.user = user

    def __str__(self):
        return self.user.username