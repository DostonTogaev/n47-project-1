from django.contrib import admin
from django.urls import path
from app.views import index, product_detail

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', product_detail, name='product_detail'),
]
