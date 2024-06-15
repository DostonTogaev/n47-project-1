
from django import forms

from app.models import Product, Customer


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()
    rating = forms.FloatField()
    discount = forms.IntegerField()
    quantity = forms.IntegerField()


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['name', 'description', 'price', 'rating', 'discount', 'quantity']
        exclude = ()
class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ()

class EdiytCustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']

