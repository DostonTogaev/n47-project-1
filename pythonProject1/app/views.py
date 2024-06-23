from django.shortcuts import render, redirect, get_object_or_404
from app.models import Product, Customer
from app.forms import CustomerModelForm, ProductModelForm, EdiytCustomerModelForm
# Create your views here.


def index(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'app/index.html', context)

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    attributes = product.attributes.all()

    context = {
        'product': product,
        'attributes': attributes
    }

    return render(request, 'app/product-details.html', context)


def add_product(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'app/add-product.html', context)


