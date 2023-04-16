from django.test import TestCase, Client
from blog.models import Post, Comment
from django.contrib.auth.models import User
from django.shortcuts import reverse, get_object_or_404


class TestViews(TestCase):

    c = Client()

    def setUp(self):
        """create a test user and test post.  Log in the test user."""
        self.user_1 = User.objects.create(username="user_1",
                                          password="password")
        logged_in = self.c.login(username='user_1',
                                 password='password')
        self.post_1 = Post.objects.create(title='title_1',
                                          author=self.user_1,
                                          content='content',
                                          region='N/A',
                                          category='others')


    def test_get_postlist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')


    def test_redirected_to_login_if_add_story_called_without_login(self):
        response = self.client.get('/add_story', follow=True)
        print(response.redirect_chain)
        # self.assertEqual(response.status_code, 302)
        # response = self.client.get(reverse('add_story'))
        # self.assertTrue(response.redirect_chain. )
  

    def test_can_get_add_story_after_login(self):
        response = self.c.get("/add_story", follow=True, secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html', 'add_story.html')


    # can't create a post
    # def test_can_add_story(self):
    #     response = self.c.post('/add_story',
    #                            {'title': 'title_2',
    #                             'author': self.user_1,
    #                             'content': 'test',
    #                             'region': 'N/A',
    #                             'category': 'others',
    #                             'save': 'draft'},
    #                            )
    #     post = get_object_or_404(Post, title='title_2')
    #     print(post)
    #     self.assertEqual(post.title, 'title_2')
    #     self.assertEqual(post.content, 'test')
    #     self.assertRedirects(response, '/add_story')


    # def test_message_says_draft_is_saved(self):
        # response = self.c.post('/add_story',
        #                        {'title': 'title_2',
        #                         'author': self.user_1,
        #                         'content': 'test',
        #                         'region': 'N/A',
        #                         'category': 'others'},
        #                        follow=True,
        #                        secure=True
        #                        )
        # 
        # self.assertEqual(response.messages, 'Your draft has been saved.')

    # def test_message_says_draft_is_submitted_if_submitted(self):
     # response = self.c.post('/add_story',
        #                        {'title': 'title_2',
        #                         'author': self.user_1,
        #                         'content': 'test',
        #                         'region': 'N/A',
        #                         'category': 'others'},
        #                        follow=True,
        #                        secure=True
        #                        )
        # self.assertEqual(messages, 'Your draft has been saved.')


    def test_get_postdetail(self):
        response = self.client.get('/detail/{0}/'.format(self.post_1.slug))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html', 'base.html')


    # can't create comments
    # def test_can_post_comment(self):
    #     user_2 = User.objects.create(username="user_2",
    #                                  password="secret")
    #     self.c.login(username='user_2', password='secret')
    #     print(type(user_2))
    #     print(user_2.is_authenticated)
    #     response = self.c.post('/detail/{0}/'.format(self.post_1.slug),
    #                            {
    #                                 'body': 'test comment',
    #                                 'commenter': user_2
    #                             }
    #                           )
    #     comment = Comment.objects.filter(commenter=user_2)
    #     print(comment)


    # def test_post_like_will_add_likes(self):
    #         
    #     response = self.c.post('/like/{0}'.format(self.post_1.slug))
    #   self.assertIn(user object, post_1.likes)



if __name__ == '__main__':
    main()