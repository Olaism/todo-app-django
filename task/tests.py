from django.test import TestCase
from django.urls import reverse, resolve

from .forms import CategoryForm
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
        
    def test_view_has_form(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')
        
    def test_view_has_correct_form_instance(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CategoryForm)
    
class CategoryCreatePostTests(TestCase):
    def setUp(self):
       self.url = reverse("category_new")
    
    def test_new_category_valid_post_data(self):
        response = self.client.post(self.url, {'title': 'Work'})
        self.assertRedirects(response, "/")
        self.assertTrue(Category.objects.exists())
        
    def test_new_category_invalid_post_data(self):
        response = self.client.post(self.url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_new_category_empty_fields_post_data(self):
        response = self.client.post(self.url, {'title': ''})
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Category.objects.exists())
 
 
 
 
 
    