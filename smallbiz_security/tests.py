from django.test import TestCase, Client
from .models import (Source, Category, Resource)

# Create your tests here.

# simple unittest


class TestSimpleComponent(TestCase):
    def test_basic_sum(self):
        assert 1+1 == 2

# testing models


class TestSourceModel(TestCase):
    def test_source_model(self):
        source = Source.objects.create(SourceName='CISA')
        self.assertIsInstance(source, Source)


class TestCategoryModel(TestCase):
    def test_category_model(self):
        category = Category.objects.create(CategoryName='General Information')
        self.assertIsInstance(category, Category)


# testing views


class TestMainView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_view(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
