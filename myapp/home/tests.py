from django.test import TestCase
from myapp.item.models import *
from . import views
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.
from .serializers import *

class ProductsTest(TestCase):
    fixtures = ['myapp/item/fixtures/app-data.json']

    def test_required_empty_key_return_404(self):
        response = self.client.get('/products')
        print("test_required_empty_key_return_404")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_required_bad_value_return_404(self):
        response = self.client.get('/products?skin_type=bad_value')
        print("test_required_bad_value_return_404")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_required_params_return_200(self):
        list = ['dry','oily','sensitive']
        print("test_required_params_return_200")
        for skin_type in list:
            response = self.client.get(f'/products?skin_type=dry&category={skin_type}')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_params_category_return_200(self):
        list = ['basemakeup','maskpack','skincare','suncare']
        print("test_params_category_return_200")
        for category in list:
            response = self.client.get(f'/products?skin_type=dry&category={category}')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_params_page_return_200(self):
        print("test_params_page_return_200")
        for page in range(1,100):
            response = self.client.get(f'/products?skin_type=dry&page={page}')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_params_exclude_ingredient_return_200(self):
        print("test_params_exclude_ingredient_return_200")
        ingredient_obj = Ingredient.objects.all()
        serializers = IngredientSerializer(ingredient_obj, many=True)
        for ingredient in serializers.data:
            response = self.client.get('/products?skin_type=dry&exclude_ingredient=%s' %ingredient['name'])
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_params_include_ingredient_return_200(self):
        print("test_params_include_ingredient_return_200")
        ingredient_obj = Ingredient.objects.all()
        serializers = IngredientSerializer(ingredient_obj, many=True)
        for ingredient in serializers.data:
            response = self.client.get('/products?skin_type=dry&include_ingredient=%s' %ingredient['name'])
            self.assertEqual(response.status_code, status.HTTP_200_OK)




class ProductDetailTest(TestCase):
    fixtures = ['myapp/item/fixtures/app-data.json']

    def test_bad_pk_return_404(self):
        print("test_required_bad_pk")
        list = ["", "as", "한글"]
        for pk in list:
            response = self.client.get(f'/product/{pk}')
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_range_over_pk_return_404(self):
        print("test_required_bad_pk")
        response = self.client.get('/product/1001')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_required_empty_key_return_404(self):
        response = self.client.get('/product/1')
        print("test_required_empty_key_return_404")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_required_bad_value_return_404(self):
        response = self.client.get('/product/1?skin_type=bad_value')
        print("test_required_bad_value_return_404")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_required_params_return_200(self):
        print("test_required_bad_pk")
        list = ['dry','oily','sensitive']
        for skin_type in list:
            response = self.client.get(f'/product/1?skin_type={skin_type}')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_range_in_pk_return_404(self):
        print("test_required_bad_pk")
        for pk in range(1,1000):
            response = self.client.get(f'/product/{pk}?skin_type=dry')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_required_success_return_200(self):
        print("test_required_bad_pk")
        list = ['dry','oily','sensitive']
        for skin_type in list:
            response = self.client.get(f'/product/1?skin_type={skin_type}')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
