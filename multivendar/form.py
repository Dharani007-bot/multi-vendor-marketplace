from django import forms
from .models import Vendor, Product

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = [
            'vendor_name',
            'company_name',
            'company_logo'
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'description',
            'price',
            'product_image'
        ]