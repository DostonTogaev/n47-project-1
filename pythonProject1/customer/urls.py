from django.urls import path
from customer.views.views import custemer, add_customer, customer_detail, customer_delete, customer_edit
from customer.views.auth import login_page, logout_view

urlpatterns = [
    path('customer', custemer, name='customer'),
    path('add-customer/', add_customer, name='add_customer'),
    path('customer-detail/<int:customer_id>', customer_detail, name='customer-detail'),
    path('delete/<int:customer_id>', customer_delete, name='delete'),
    path('edit-customer/<int:customer_id>', customer_edit, name='edit_customer'),
    path('login-page/', login_page, name='login'),
    path('logout/', logout_view, name='logout')
]
