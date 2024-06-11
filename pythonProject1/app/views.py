from django.shortcuts import render
from app.models import Product
# Create your views here.


def index(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'app/index.html', context)

def product_detail(request, pk):
    product = Product.objects.get(id=pk)

    context={
        'product': product
    }

    return render (request, 'app/product-details.html', context)