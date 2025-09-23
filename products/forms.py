from django import forms
from .models import Product  # Make sure you have a Product model

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']  # adjust to your Product model fields
