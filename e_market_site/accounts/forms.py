from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Seller, User
"""
TODO: add phone mask in style '+_(___)__-__-___'
TODO: add e-mail mask in style '*@*'
"""
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']

        if commit:
            user.save()

        return user



class SellerRegisterForm(forms.ModelForm):
    shop_name = forms.CharField(max_length=255)
        
    class Meta:
        model = Seller
        fields = (
            'shop_name',
        )
