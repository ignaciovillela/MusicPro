from django.test import Client, TestCase
from django.urls import reverse

from shop.models import Category, Product


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name='fastfood',
            slug='fastfood1',
        )
        self.product = Product.objects.create(
            id=20,
            category=self.category,
            name='testproduct',
            slug='testproduct',
            description='my test product',
            image='static/core/img/logo.png',
            price=30,
        )

    def test_product_list_view(self):
        response = self.client.get(reverse('shop:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/list.html')

    def test_product_list_by_category_view(self):
        response = self.client.get(reverse(
            'shop:product_list_by_category',
            kwargs={"category_slug": "fastfood1"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/list.html')

    def test_product_detail_view(self):
        response = self.client.get(reverse(
            'shop:product_detail',
            kwargs={'id': 20, 'slug': 'testproduct'})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/detail.html')

    def test_product_detail_view_error(self):
        response = self.client.get(reverse(
            'shop:product_detail',
            kwargs={'id': 21, 'slug': 'nottestproduct'})
        )
        self.assertEqual(response.status_code, 404)
