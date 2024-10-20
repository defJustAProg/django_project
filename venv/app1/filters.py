import django_filters
from app1.models import Customer, Order, Product
from django.db.models import Q

class Customer(django_filters.FilterSet):
    login = django_filters.CharFilter(lookup_expr='icontains',label='Название')
    class Meta:
        model = Customer
        fields = ['login', 'registration_date']

class Order(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(field_name='product__price', label='Цена от и до')
    available = django_filters.BooleanFilter(method='filrer_available', label='Кольчество товара на складе')
    class Meta:
        model = Order
        fields = ['order_date','price_range', 'available']

    def filrer_available(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(product__count_of_products_on_warehouse__gt = 0)
        return queryset.filter(product__count_of_products_on_warehouse=0)


class Product(django_filters.FilterSet):
    term = django_filters.CharFilter(method='filter_term', label='Совпадение')

    class Meta:
        model = Product
        fields =['name', 'description']

    def filter_term(self, queryset, name, value):
        criteria = Q()
        for term in value.split():
            criteria &= Q(name__icontains=term) | Q(description__icontains=term)
        return queryset.filter(criteria).distinct()
