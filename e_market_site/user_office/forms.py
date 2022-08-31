from django import forms
from shop.models import Product
class AddProductForm(forms.ModelForm):        
    class Meta:
        model = Product
        fields = (
            'name',
            'category',
            'description',
            'price',
            'main_image',
            'count'
        )
