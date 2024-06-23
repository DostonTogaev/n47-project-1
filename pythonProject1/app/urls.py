from django.contrib import admin
from django.urls import path
from app.views import index, product_detail,  add_product


urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', product_detail, name='product_detail'),
    path('add-product/', add_product, name='add_product'),

]
