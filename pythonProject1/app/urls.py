from django.contrib import admin
from django.urls import path
from app.views import index, product_detail, custemer, add_product, add_customer, customer_detail, customer_delete, customer_edit

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', product_detail, name='product_detail'),
    path('add-product/', add_product, name='add_product'),
    path('customer', custemer, name='customer'),
    path('add-customer/', add_customer, name='add_customer'),
    path('customer-detail/<int:customer_id>', customer_detail, name='customer-detail'),
    path('delete/<int:customer_id>', customer_delete, name='delete'),
    path('edit-customer/<int:customer_id>', customer_edit, name='edit_customer'),
]
