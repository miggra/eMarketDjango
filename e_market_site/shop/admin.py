from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Card, Order, Product
from accounts.models import Customer, Seller, User




admin.site.register(Customer)


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "get_groups")
    def get_groups(self, user):
        return "\n".join([g.name for g in user.groups.all()])
    
admin.site.register(User, CustomUserAdmin)


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
