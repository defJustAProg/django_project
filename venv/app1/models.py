from django.db import models
import uuid

# Create your models here.
class Customer(models.Model):
    login = models.CharField(verbose_name="Логин", max_length=255,primary_key=True)
    email = models.EmailField(verbose_name="email")
    registration_date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    class Meta:
        verbose_name = 'Клиент'

    def __str__(self):
        return f"Customer {self.login}"

class Product(models.Model):
    UUID = models.UUIDField(verbose_name="UUID", primary_key=True, default=uuid.uuid4)
    name = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание")
    count_of_products_on_warehouse = models.IntegerField(verbose_name="Количество товаров на складе")
    price = models.IntegerField(verbose_name='Стоимость')
    image = models.ImageField(verbose_name='Изображение', blank=True)
    storage = models.ForeignKey(
        to='Storage',
        verbose_name="Склад",
        on_delete=models.CASCADE,
        related_name='products'
    )

    class Meta:
        verbose_name='Продукт'

    def __str__(self):
        return f"Product {self.name}"

class Order(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    product = models.ForeignKey(
        to='Product',
        verbose_name="Продукт",
        on_delete=models.CASCADE,
        null=True  # Позволяет полю быть пустым
    )
    customer = models.ForeignKey(
        to='Customer',
        verbose_name="Клиент",
        on_delete=models.SET_NULL,
        null=True  # Позволяет полю быть пустым, если клиент будет удален
    )
    order_date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    status_of_delivery = models.CharField(verbose_name="остояние доставки", max_length=255)
    feedback = models.TextField(verbose_name="Отзыв", blank=True)
    count_of_positions = models.IntegerField(verbose_name="Количество товаров в заказе")

    class Meta:
        verbose_name='Заказ'

    def __str__(self):
        return f"Order {self.product}"




class Storage(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название склада", primary_key=True)

    class Meta:
        verbose_name = 'Склад'

    def __str__(self):
        return self.name