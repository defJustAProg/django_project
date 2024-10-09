from django.contrib import admin
from app1 import models
# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('UUID', 'name')

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer')

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('login', 'email')

@admin.register(models.Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('name',)