from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        """create a test user"""
        User.objects.create(username="test", password="password")
        

    def test_get_postlist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')


    # It's testing login mixin, not View. ok in this file?
    def test_cannot_get_add_story_without_login(self):
        response = self.client.get('/add_story')
        self.assertEqual(response.status_code, 301)


    # def test_can_get_add_story_after_login(self):

    #     # login 
    #     response = self.client.get('/add_story')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'add_story.html')