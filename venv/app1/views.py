from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello from app1")

def url2(request):
    return HttpResponse("url2 from app1")

def url3(request):
    return HttpResponse("url3")


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Customer, Product, Order, Storage

# Customer Views
class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['login', 'email']

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['login', 'email']

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')

# Product Views
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'description', 'count_of_products_on_warehouse', 'price', 'image', 'storage']

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'description', 'count_of_products_on_warehouse', 'price', 'image', 'storage']

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

# Order Views
class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_form.html'
    fields = ['product', 'customer', 'status_of_delivery', 'feedback', 'count_of_positions']

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_form.html'
    fields = ['product', 'customer', 'status_of_delivery', 'feedback', 'count_of_positions']

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('order_list')

# Storage Views
class StorageListView(ListView):
    model = Storage
    template_name = 'storage_list.html'

class StorageDetailView(DetailView):
    model = Storage
    template_name = 'storage_detail.html'

class StorageCreateView(CreateView):
    model = Storage
    template_name = 'storage_form.html'
    fields = ['name']

class StorageUpdateView(UpdateView):
    model = Storage
    template_name = 'storage_form.html'
    fields = ['name']

class StorageDeleteView(DeleteView):
    model = Storage
    template_name = 'storage_confirm_delete.html'
    success_url = reverse_lazy('storage_list')