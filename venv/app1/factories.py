import factory
from factory.django import ImageField
from app1.models import Customer, Product, Storage

class StorageFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')

    class Meta:
        model = Storage
class CustomerFactory(factory.django.DjangoModelFactory):
    login = factory.Faker('user_name')
    email = factory.Faker('email')
    class Meta:
        model = Customer

class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')
    description = factory.Faker('text')
    count_of_products_on_warehouse = factory.Faker('random_int', min=0, max=100)
    price = factory.Faker('random_number', digits=5, fix_len=True)
    storage = factory.SubFactory(StorageFactory)

    class Meta:
        model = Product