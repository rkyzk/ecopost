from django.test import TestCase, Client
from .admin import PostAdmin
from blog.models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse, get_object_or_404


class TestAdmin(TestCase):

    def setUp(self):
        """create a test user and test post."""
        self.user1 = User.objects.create_user(username="user1")
        self.user1.set_password('password')
        self.user1.save()
        self.post1 = Post.objects.create(title='title1',
                                         author=self.user1,
                                         content='content',
                                         region='N/A',
                                         category='others')

    def test_func_publish_posts_will_set_status_2(self):
        posts = Post.objects.all()
        publish_posts(request, posts)
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0].status, 2)
