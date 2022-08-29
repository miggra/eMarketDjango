from datetime import datetime
import email
import logging
from pyexpat import model
from random import choices
from tkinter import CASCADE
from tokenize import Name
from django.db import models
from accounts.models import Seller, Customer
# Create your models here.

    

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(null=True, blank=True)
    main_image = models.ImageField()
    count = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE
    )

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

class Order(models.Model):
    product = models.ManyToManyField(
        Product
    )
    date_time_created = models.DateTimeField()
    class Statuses(models.IntegerChoices):
        RESERVED = 1, 'Зарезервирован'
        PAID = 2, 'Оплачен'
        SHIPPED = 3, 'Отправлен'
        WAIT_FOR_CUSTOMER = 4, 'Ожидает получения'
        RECIEVED = 5, 'Получен'
    status = models.IntegerField(
        null=False,
        default=Statuses.RESERVED,
        choices=Statuses.choices
        ) 

class Card(models.Model):    
    product = models.ManyToManyField(Product)