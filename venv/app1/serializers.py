from rest_framework import serializers
from app1 import models

class Customer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'

class Product(serializers.ModelSerializer):
    Storage = models.Storage
    class Meta:
        model = models.Product
        fields = '__all__'

class Order(serializers.ModelSerializer):
    product = models.Product
    customer = models.Product
    class Meta:
        model = models.Order
        fields = '__all__'