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

def custemer(request):
    customers = Customer.objects.all()

    context = {
        'customers': customers
    }
    return render(request, 'app/customer.html', context)

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

def add_customer(request):
    form = CustomerModelForm()
    if request.method == 'POST':
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer')
    context = {
        'form': form,
    }
    return render(request, 'app/add-customer.html', context)

def customer_detail(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    context = {
        'customer': customer
    }
    return render(request, 'app/customer-detail.html', context)

def customer_delete(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if customer:
        customer.delete()
        return redirect('index')

    context = {
        'customer': customer,
    }
    return render('app/customer.html', context)

def customer_edit(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = EdiytCustomerModelForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer', customer_id)
    context = {
        'customer': customer,
    }
    return render(request, 'app/edit-customer.html', context)


