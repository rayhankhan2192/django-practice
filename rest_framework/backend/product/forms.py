from django import forms
from .models import Product

class Product_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price'
        ]