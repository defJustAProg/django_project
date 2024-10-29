from rest_framework import serializers
from app1 import models

class Customer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'

class Storage(serializers.ModelSerializer):
    class Meta:
        model = models.Storage
        fields = '__all__'

class Product(serializers.ModelSerializer):
    storage = Storage()
    class Meta:
        model = models.Product
        fields = '__all__'

class Order(serializers.ModelSerializer):
    product = Product()
    customer = Customer()
    class Meta:
        model = models.Order
        fields = '__all__'

