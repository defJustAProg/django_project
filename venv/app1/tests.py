from django.test import TestCase
from django.urls import reverse
from app1 import factories
from app1.models import Customer, Product, Storage

class App1TestCase(TestCase):
    def setUp(self):
        self.storage = factories.StorageFactory()
        self.customer = factories.CustomerFactory()
        self.product = factories.ProductFactory()

    def test_customer_list(self):
        url = reverse('customer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer_list.html')
        print(response)

    def test_customer_create(self):
        url = reverse('customer_form')
        response = self.client.put(url,{'login': 'new_login','email': 'email@mail.ru'})
        self.assertEqual(response.status_code, 201)
        self.assertTemplateUsed(response, 'customer_form.html')

    def test_get_customer_detail(self):
        url = reverse('customer_detail',kwargs={'pk': self.customer.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print(response)

    def test_update_customer(self):
        url = reverse('customer_update', kwargs={'pk': self.customer.login})
        old_login = self.customer.login
        old_email = self.customer.email
        response = self.client.post(url, {'login': 'new_login', 'email': 'new_email'})
        self.customer.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(self.customer.login, old_login)

