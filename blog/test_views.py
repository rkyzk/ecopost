from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        """create test users and posts"""
        self.user_1 = User.objects.create(username="user_1", password="password")
    #     self.user_2 = User.objects.create(username="user_2", password="password")
    #     self.post1 = Post.objects.create(title="title_1",
    #                         author=self.user_1,
    #                         content="test sentences")
    #     self.post2 = Post.objects.create(title="title_2",
    #                         author=self.user_2,
    #                         content="test 2 sentences")
    #     self.post3 = Post.objects.create(title="title_3",
    #                         author=self.user_1,
    #                         content="test 3 sentences")
    #     self.post4 = Post.objects.create(title="title_4",
    #                         author=self.user_2,
    #                         content="test 4 sentences")
       

    def test_get_postlist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')


    # It's testing login mixin, not View. ok in this file?
    # def test_cannot_get_add_story_without_login(self):
    #     response = self.client.get('/add_story')
    #     self.assertEqual(response.status_code, 301)

        # print(self.request.user.is_authenticated)
        # print(dir(self.request.user))
   

    def test_can_get_add_story_after_login(self):
        response = self.slient.get('/add_story')
        self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'add_story.html')


if __name__ == '__main__':
    main()