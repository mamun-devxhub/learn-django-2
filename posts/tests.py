"""posts/tests.py"""
from django.test import TestCase
from django.urls import reverse  # new
from .models import Post


class PostModelTest(TestCase):
    """PostModelTest"""

    def setUp(self):
        """setUp"""
        Post.objects.create(text='just a test')

    def test_text_content(self):
        """test_text_content"""
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')


class HomePageViewTest(TestCase):
    """HomePageViewTest"""
    def setUp(self):
        """"SetUp"""
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        """test_view_url_exists_at_proper_location"""
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        """test_view_url_by_name"""
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        """test_view_user_correct_template"""
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

