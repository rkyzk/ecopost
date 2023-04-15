from django.test import TestCase, Client
from blog.models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse, get_object_or_404

class TestViews(TestCase):

    c = Client()

    def setUp(self):
        """create test users and posts"""

        self.user_1 = User.objects.create(username="user_1", password="password")
        logged_in = self.c.login(username='user_1', password='password')
    

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
       

        # # confirm user is logged in
        # self.assertTrue(log_in)
        # self.assertTrue(self.user.is_staff)




    def test_get_postlist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')


    # It's testing login mixin, not View. ok in this file?
    def test_cannot_get_add_story_without_login(self):
        response = self.client.get('/add_story')
        print(response.status_code)
   

    def test_can_get_add_story_after_login(self):
        page = self.c.get("/add_story", follow=True, secure=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'base.html', 'add_story.html')


    def test_can_add_story(self):
        # page = self.c.get("/add_story", follow=True, secure=True)
        response = self.c.post("/add_story",
                           data = {
                               "title": 'title_2',
                               "content": "test",
                               "region": "N/A",
                               "category": "others"
                               },
                           follow = True,
                           secure = True)
        self.assertEqual(response.status_code, 200)
        post = get_object_or_404(Post, title='title_2')
        self.assertEqual(post.title, 'title_2')
        self.assertEqual(post.content, 'test')
        self.assertTemplateUsed(response, "add_story.html")



        # response = self.client.login(username="user_1", password="password")
        # print(self.user_1.is_authenticated)
        # print(dir(self.client))
        # response = self.client.get('/add_story')
        # self.assertEqual(response.status_code, 200)
        # 


if __name__ == '__main__':
    main()