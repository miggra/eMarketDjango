from datetime import datetime
import email
import logging
from pyexpat import model
from random import choices
from tokenize import Name
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(null=True)
    main_image = models.ImageField()
    count = models.PositiveIntegerField()


class Comment(models.Model):
    text = models.TextField()
    rating = models.IntegerField(
        null = False,
        default = 1
    )
    product = models.ForeignKey(
        Product,
        on_delete = models.CASCADE,
    )
    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_rating_range",
                check=models.Q(rating__range=(1, 5)),
            ),
        ]
    

class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    date_time = models.DateTimeField() 


class User(AbstractUser):
    pass


# class User(models.Model):
#     name
#     login 
#     password
#     phone
#     email

#     class Meta:
#         abstract = True


