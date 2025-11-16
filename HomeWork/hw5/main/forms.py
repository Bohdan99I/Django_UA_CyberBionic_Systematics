from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Product, ProductReview

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логін', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class CustomAuthForm(forms.Form):
    username = forms.CharField(label='Ім’я користувача')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'stock']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['product', 'user_email', 'description', 'rating', 'review_type', 'phone_number', 'image']
