from django.urls import path
from .views import (
    index,
    url2,
    url3,
    CustomerListView,
    CustomerDetailView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    OrderListView,
    OrderDetailView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    StorageListView,
    StorageDetailView,
    StorageCreateView,
    StorageUpdateView,
    StorageDeleteView,
)

urlpatterns = [
    path('', index),
    path('url2/', url2),
    path('url3/', url3),

    # Customer URLs
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<str:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/update/<str:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/delete/<str:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),

    # Product URLs
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<uuid:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<uuid:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<uuid:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    # Order URLs
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),
    path('orders/update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('orders/delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),

    # Storage URLs
    path('storages/', StorageListView.as_view(), name='storage_list'),
    path('storages/<str:pk>/', StorageDetailView.as_view(), name='storage_detail'),
    path('storages/create/', StorageCreateView.as_view(), name='storage_create'),
    path('storages/update/<str:pk>/', StorageUpdateView.as_view(), name='storage_update'),
    path('storages/delete/<str:pk>/', StorageDeleteView.as_view(), name='storage_delete'),
]