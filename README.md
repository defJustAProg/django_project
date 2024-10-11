# Django project

---
1 Задание

 from app1.models import Customer, Product, Order
 name2=Customer.objects.create(login='name2',email='name2@mail.ru') 
 storage = Storage.objects.get(name='First_storage')
 product2=Product.objects.create(name ='product2', description ='bla-bla',count_of_products_on_warehouse =50, price =75, storage=storage) 
 order=Order.objects.create(product =product2, customer = name2, status_of_delivery ='В пути', count_of_positions = 1) 
 Customer.objects.all()
`<QuerySet [<Customer: Customer user1>, <Customer: Customer name2>]>
` Product.objects.all()  
`<QuerySet [<Product: Product Product1>, <Product: Product product2>]>
` Storage.objects.all() 
`<QuerySet [<Storage: First_storage>]>`
 Order.objects.all()   
`<QuerySet [<Order: Order Product Product1>, <Order: Order Product product2>]>`
 
 ---
 2 Задание

 Product.objects.filter(name='Product1') 
`<QuerySet [<Product: Product Product1>]>`
 Order.objects.exclude(product=product2)   
`<QuerySet [<Order: Order Product Product1>]>`
 Product.objects.order_by('price')                      
`<QuerySet [<Product: Product product2>, <Product: Product product3>, <Product: Product product4>, <Product: Product Product1>]>`
 Product.objects.order_by('-price') 
`<QuerySet [<Product: Product Product1>, <Product: Product product2>, <Product: Product product3>, <Product: Product product4>]>
`
---
3 Задание

 Order.objects.filter(product__name='Product1') 
`<QuerySet [<Order: Order Product Product1>]>`
 Order.objects.filter(customer__login='user1')     
`<QuerySet [<Order: Order Product Product1>]>`
 Order.objects.select_related('customer').values('id', 'customer__login')     
`<QuerySet [{'id': 2, 'customer__login': 'name2'}, {'id': 1, 'customer__login': 'user1'}]>`
 Order.objects.select_related('product').values_list('id', 'product__name') 
`<QuerySet [(2, 'product2'), (1, 'Product1')]>`

---
4 Задание

from django.db.models import Q
 Product.objects.filter(Q(name__icontains='Product1') | Q(Q(price__lt=100)))  
`<QuerySet [<Product: Product Product1>, <Product: Product product2>, <Product: Product product3>, <Product: Product product4>]>`
 Product.objects.filter(Q(name__icontains='Product1') & Q(Q(price__gt=100))) 
`<QuerySet [<Product: Product Product1>]>`
 Product.objects.filter(Q(name__icontains='Product1') & Q(Q(price__gt=100))).exclude(price__gt=100) 
`<QuerySet []>`

---
5 Задание

from django.db.models import Avg, Max, Min

 Product.objects.aggregate(average_price=Avg('price'), max_price=Max('price'), min_price=Min('price'))
`{'average_price': 1306.25, 'max_price': 5000, 'min_price': 75}`
from django.db.models import Count

 customer_orders = Customer.objects.annotate(order_count=Count('order'))
 for customer in customer_orders:                                          
...     print(f"Customer: {customer.login}, Order Count: {customer.order_count}")
... 
`Customer: name2, Order Count: 1
Customer: user1, Order Count: 1`

 storage_products_count = Storage.objects.annotate(product_count=Count('products'))
 for storage in storage_products_count:
...     print(f"Storage: {storage.name}, Product Count: {storage.product_count}")
... 
`Storage: First_storage, Product Count: 4`