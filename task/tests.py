from django.test import TestCase
from django.urls import reverse, resolve

from .models import Category
from .views import category_list, category_detail, category_new

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
    def setUp(self):
        self.url = reverse('category_new')
        self.response = self.client.get(self.url)
    def test_new_category_view_success_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_new_category_url_resolves_new_category_view(self):
        view = resolve("/category/new/")
        self.assertEquals(view.func, category_new)
    
    
    
    
    