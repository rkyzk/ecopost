from django.test import TestCase, Client
from blog.models import Post, Comment
from django.contrib.auth.models import User
from django.shortcuts import reverse, get_object_or_404


class TestViews(TestCase):


    def setUp(self):
        """create a test user and test post.  Log in the test user."""
        self.user1 = User.objects.create_user(username="user1")
        self.user1.set_password('password')
        self.user1.save()
        self.c = Client()
        logged_in = self.c.login(username='user1', password='password')
        self.post1 = Post.objects.create(title='title1',
                                         author=self.user1,
                                         content='content',
                                         region='N/A',
                                         category='others'
                                        )


    def test_get_postlist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')


    def test_redirected_to_login_if_add_story_called_without_login(self):
        response = self.client.get(reverse('add_story'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))
  

    def test_can_get_add_story_after_login(self):
        response = self.c.get("/add_story/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html', 'add_story.html')


    def test_can_add_story(self):
        response = self.c.post('/add_story/',
                                {
                                    'title': 'title2',
                                    'content': 'test',
                                    'region': 'N/A',
                                    'category': 'others',
                                    'save': 'draft'
                                },
                              )
        post = Post.objects.filter(slug='title2').first()
        self.assertEqual(post.title, 'title2')
        self.assertEqual(post.content, 'test')
        self.assertRedirects(response, '/detail/post{0}/'.format(post.pk))


    # def test_message_says_draft_is_saved(self):
    #     response = self.c.post('/add_story',
    #                            {'title': 'title_2',
    #                             'author': self.user_1,
    #                             'content': 'test',
    #                             'region': 'N/A',
    #                             'category': 'others'},
    #                            follow=True,
    #                            secure=True
    #                            )
        
    #     self.assertEqual(response.messages, 'Your draft has been saved.')

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


    def test_get_detail_page(self):
        response = self.client.get('/detail/post1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html', 'base.html')


    def test_post_detail_POST_can_post_comment(self):
        response = self.c.post('/detail/post1/',
                               {
                                    'body': 'test comment'
                                }
                               )
        comment = Comment.objects.filter(commenter=self.user1).first()
        self.assertEqual(comment.body, 'test comment')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html', 'base.html')



    def test_post_like_will_add_likes(self):
        user2 = User.objects.create_user(username="user2")
        user2.set_password('password2')
        user2.save()
        c = Client()
        logged_in = c.login(username='user2', password='password2')
        response = self.c.post(reverse('post_like', args=[1]))
        self.post1.save()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/detail/post1/')
        # self.assertTrue(self.post1.likes.filter(id=user2.id).exists())


    # should get 403
    # def test_get_update_post(self):
    #     response = self.client.get('/update/post{0}'.format(self.post_1.pk), follow=True)
    #     print(response.status_code)
    #     print(response.redirect_chain)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTrue(response.url.startswith('/accounts/login/'))


    # def test_can_get_my_page_if_user(self):
    #     response = self.c.get('/mypage/user{0}'.format(self.user_1.id))
    #     # self.assertEqual(response.status_code, 200)
    #     print(self.user_1.is_authenticated)
    #     print(response.url)
        # self.assertTemplateUsed(response, 'my_page.html', 'base.html')
        

    # should get 403
    # def test_cannot_get_my_page_if_not_the_user(self):
    #     user_2 = User.objects.create(username="user_2",
    #                                  password="pw2")
    #     self.c.login(username='user_2', password='pw2')
    #     print(user_2.is_authenticated)
    #     response = self.client.get('/mypage/user{0}'.format(self.user_1.id))
    #     print(response.status_code)


if __name__ == '__main__':
    main()