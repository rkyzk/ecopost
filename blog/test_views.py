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
                                         category='others')
        self.comment1 = Comment.objects.create(body='test comment',
                                               commenter=self.user1,
                                               post=self.post1)


    # def test_get_postlist(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'index.html', 'base.html')


    # def test_add_story_will_redirect_to_login_if_not_logged_in(self):
    #     response = self.client.get(reverse('add_story'))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTrue(response.url.startswith('/accounts/login/'))
  

    # def test_can_get_add_story_if_logged_in(self):
    #     response = self.c.get("/add_story/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'base.html', 'add_story.html')


    # def test_can_add_story(self):
    #     response = self.c.post('/add_story/',
    #                             {
    #                                 'title': 'title2',
    #                                 'content': 'test',
    #                                 'region': 'N/A',
    #                                 'category': 'others',
    #                                 'save': 'draft'
    #                             },
    #                           )
    #     post = Post.objects.filter(slug='title2').first()
    #     self.assertEqual(post.title, 'title2')
    #     self.assertEqual(post.content, 'test')
    #     self.assertRedirects(response, '/detail/title2/')


    # def test_add_story_GET_will_set_status_to_1_if_submit_clicked(self):
    #     response = self.c.post('/add_story/',
    #                             {
    #                                 'title': 'title2',
    #                                 'content': 'test',
    #                                 'region': 'N/A',
    #                                 'category': 'others',
    #                                 'submit': 'complete'
    #                             },
    #                           )
    #     post = Post.objects.filter(slug='title2').first()
    #     self.assertEqual(post.title, 'title2')
    #     self.assertEqual(post.status, 1)
    #     self.assertRedirects(response, '/detail/title2/')


    # NG def test_post_add_story_empty_input_will_raise_error(self):
    #      response = self.c.post('/add_story/',
    #                             {
    #                                 'title': '',
    #                                 'content': '',
    #                                 'region': 'N/A',
    #                                 'category': 'others',
    #                                 'save': 'draft'
    #                             },
    #                           )

    # NG def test_message_says_draft_is_saved(self):
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

    # NG def test_message_says_draft_is_submitted_if_submitted(self):
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


    # def test_can_get_detail_page(self):
    #     response = self.client.get('/detail/title1/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'post_detail.html', 'base.html')


    # def test_post_detail_POST_can_post_comment(self):
    #     response = self.c.post('/detail/title1/',
    #                            {
    #                                 'body': 'test comment'
    #                             }
    #                            )
    #     comment = Comment.objects.filter(commenter=self.user1).last()
    #     self.assertEqual(comment.body, 'test comment')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'post_detail.html', 'base.html')


    # NG def test_post_detail_POST_no_input_for_comment_will_prompt_input(self):
    #     response = self.c.post('/detail/title1/',
    #                            {
    #                                 'body': ''
    #                             }
    #                            )
    #     comment = Comment.objects.filter(commenter=self.user1)
    #     self.assertEqual(len(comment), 1)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'post_detail.html', 'base.html')
    #     # validation = 'Please fill in this field'


    # NG def test_post_detail_POST_spaces_for_comment_will_show_error_message(self):
        # response = self.c.post('/detail/title1/',
        #                        {
        #                             'body': '  '
        #                         }
        #                        )
        # comment = Comment.objects.filter(commenter=self.user1)
        # self.assertEqual(len(comment), 1)
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'post_detail.html', 'base.html')
        # how to get error message?

    # NG likes not added
    # def test_post_like_will_add_user(self):
    #     user2 = User.objects.create_user(username="user2")
    #     user2.set_password('password2')
    #     user2.save()
    #     c = Client()
    #     logged_in = c.login(username='user2', password='password2')
    #     response = self.c.post(reverse('post_like', args=['title1']))
    #     self.post1.save()
    #     post = Post.objects.filter(slug='title1').first()
    #     print(self.post1.likes.all())
    #     self.assertRedirects(response, '/detail/title1/')
        # self.assertTrue(self.post1.likes.filter(id=user2.id).exists())

    # likes will be removed, if twice hit

    # bookmark will add the user

    # bookmark twice will remove the user


    # def test_can_get_update_comment_if_right_user(self):
    #     response = self.c.get('/update_comment/comment1/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'update_comment.html', 'base.html')


    # def test_get_update_comment_will_redirect_to_login_if_not_logged_in(self):
    #     response = self.client.get('/update_comment/comment1/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTrue(response.url.startswith('/accounts/login/'))


    def test_get_update_comment_will_403_if_wrong_user(self):
        user2 = User.objects.create_user(username="user2")
        user2.set_password('password2')
        user2.save()
        c2 = Client()
        logged_in = c2.login(username='user2', password='password2')
        response = c2.get(reverse('update_comment', args=[1]))
        self.assertEqual(response.status_code, 403)


    # def test_can_update_comment(self):
    #     response = self.c.post('/update_comment/comment1/',
    #                             {'body': 'comment updated'})
    #     comment = Comment.objects.filter(commenter=self.user1).first()
    #     self.assertEqual(comment.body, 'comment updated')
    #     self.assertEqual(comment.comment_status, 1)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, '/detail/title1/')


    # def test_post_delete_comment_will_set_comment_status_to_2(self):
    #     response = self.c.post('/delete_comment/comment1/')
    #     comment = Comment.objects.filter(commenter=self.user1).first()
    #     self.assertEqual(comment.comment_status, 2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, '/detail/title1/')


    # def test_get_update_post_will_redirect_to_login_if_not_logged_in(self):
    #     response = self.client.get('/update/title1/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTrue(response.url.startswith('/accounts/login/'))


    # def test_get_update_post_will_403_if_wrong_user(self):
    #     user2 = User.objects.create_user(username="user2")
    #     user2.set_password('password2')
    #     user2.save()
    #     c2 = Client()
    #     logged_in = c2.login(username='user2', password='password2')
    #     response = c2.get('/update/title1/')
    #     self.assertEqual(response.status_code, 403)


    # def test_can_get_update_post_if_right_user(self):
    #     response = self.c.get('/update/title1/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'update_post.html', 'base.html')


    # can't update post  form.save() in views necessary?
    # def test_can_update_post(self):
    #     response = self.c.post('/update_post/',
    #                             {
    #                                 'title': 'title1',
    #                                 'content': 'content updated',
    #                                 'region': 'N/A',
    #                                 'category': 'others',
    #                                 'save': 'draft'
    #                             },
    #                           )
    #     post = Post.objects.filter(slug='title1').first()
    #     print(post)
    #     self.assertEqual(post.title, 'title1')
    #     self.assertEqual(post.content, 'content updated')
    #     self.assertRedirects(response, '/detail/title1/')


    # def test_no_change_will_not_update_post(self):


    def test_can_get_search(self):
        response = self.client.get('/search_story/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')


    # def test_search_no_input_will_(self):


    def test_can_get_more_stories(self):
        response = self.client.get('/more_stories/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'more_stories.html')

    # need to test the content of object_list?
    def test_can_get_more_stories(self):
        response = self.client.get('/more_stories/')
        # print(response.context['object_list'])


#     def test_can_get_my_page_if_user(self):
#         response = self.c.get('/mypage/user1/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'my_page.html', 'base.html')


#     def test_get_403_for_my_page_if_not_the_right_user(self): 
#         user2 = User.objects.create_user(username="user2")
#         user2.set_password('password2')
#         user2.save()
#         c2 = Client()
#         logged_in = c2.login(username='user2', password='password2')
#         response = c2.get('/mypage/user1/')
#         self.assertEqual(response.status_code, 403)


# class TestSearchView(TestCase):

#     def setUp(self):
#         """create test posts."""
#         self.user1 = User.objects.create_user(username="user1", password="pw1")
#         self.user2 = User.objects.create_user(username="user2", password="pw2")
#         self.user3 = User.objects.create_user(username="user3", password="pw3")
        
#         self.post1 = Post.objects.create(title='title1',
#                                          author=self.user1,
#                                          content='content',
#                                          region='N/A',
#                                          category='others')
        
#         self.post2 = Post.objects.create(title='title2',
#                                          author=self.user2,
#                                          content='content',
#                                          region='N/A',
#                                          category='others')
        
#         self.post3 = Post.objects.create(title='title3',
#                                          author=self.user3,
#                                          content='content',
#                                          region='N/A',
#                                          category='others')

#     def test_search_by_title_contains_will_get_right_posts(self):
#         response = self.client.get('search',
#                                     {'title_input': '1',
#                                      'title_field': 'contains',
#                                      'search': 'search'})
        # print(response.context['categories'])
        

if __name__ == '__main__':
    main()