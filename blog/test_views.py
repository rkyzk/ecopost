from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        """create test users and posts"""
        self.user_1 = User.objects.create(username="user_1", password="password")
        self.user_2 = User.objects.create(username="user_2", password="password")
        self.post1 = Post.objects.create(title="title_1",
                            author="user_1",
                            content="test sentences")
        self.post2 = Post.objects.create(title="title_2",
                            author="user_2",
                            content="test 2 sentences")
        self.post3 = Post.objects.create(title="title_3",
                            author="user_3",
                            content="test 3 sentences")
        self.post4 = Post.objects.create(title="title_4",
                            author="user_4",
                            content="test 4 sentences")
       

    def test_get_postlist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')


    # ?
    def queryset_contains_posts_with_featured_flag_set_to_true(self):
        """how to test if all posts displayed on home have featured flag
           set to True"""
        post_list = [self.post1, self.post2, self.post3, self.post4,]
        for post in post_list:
            post.featured_flag = True



    # It's testing login mixin, not View. ok in this file?
    def test_cannot_get_add_story_without_login(self):
        response = self.client.get('/add_story')
        self.assertEqual(response.status_code, 301)


    # def test_can_get_add_story_after_login(self):

    #     # login
    #     response = self.client.get('/add_story')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'add_story.html')