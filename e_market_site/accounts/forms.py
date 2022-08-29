from django import forms
"""
TODO: add phone mask in style '+_(___)__-__-___'
TODO: add e-mail mask in style '*@*'
"""
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    phone_number = forms.CharField()
    password = (forms 
        .CharField(widget=forms.PasswordInput, max_length=255))
    confirm_password = (forms
        .CharField(widget=forms.PasswordInput, max_length=255))


class SellerRegisterForm(RegisterForm):
    shop_name = forms.CharField(max_length=255)
        

