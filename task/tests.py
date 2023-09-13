from django.test import TestCase
from django.urls import reverse, resolve

from .models import Category
from .views import category_list, category_detail

class CategoryListTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title="Testing")
        url = reverse("category_list")
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_resolve_correct_url(self):
        view = resolve("/")
        self.assertEquals(view.func, category_list)

class CategoryDetailTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='Testing')
        url = reverse("category_detail", kwargs={'pk': self.category.pk})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_resolve_correct_url(self):
        view = resolve("/category/{0}/".format(self.category.pk))
        self.assertEquals(view.func, category_detail)


class CategoryCreateTests(TestCase):
    pass