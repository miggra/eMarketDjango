from django import forms
from shop.models import Product
class SellerRegisterForm(forms.ModelForm):        
    class Meta:
        model = Product
        fields = (
            'name',
            'category',
            'description',
            'price',
            'rating',
            'main_image',
            'count'
        )
