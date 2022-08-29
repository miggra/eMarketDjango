import imp
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Card, Order, Product
from accounts.models import Customer, Seller, User



admin.site.register(User, UserAdmin)
admin.site.register(Customer)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('shop_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('rating',)
    list_display = ('name','category', 'seller', 'rating', 'count', 'price')

    
admin.site.register(Order)
admin.site.register(Card)



# Register your models here.
