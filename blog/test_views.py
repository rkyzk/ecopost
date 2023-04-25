from django.test import TestCase, Client
from blog.models import Post, Comment
from django.contrib.auth.models import User
from django.shortcuts import reverse, get_object_or_404
from django.contrib.messages import get_messages


class TestViews(TestCase):


    def setUp(self):
        """create a test user and test post.  Log in the test user."""
        self.user1 = User.objects.create_user(username="user1")
        self.user1.set_password('password')
        self.user1.save()
        self.c = Client()
        logged_in = self.c.login(username='user1', password='password')
        self.user2 = User.objects.create_user(username="user2")
        self.user2.set_password('pw2')
        self.user2.save()
        self.c2 = Client()
        logged_in = self.c2.login(username='user2', password='pw2')
        self.post1 = Post.objects.create(title='title1',
                                         author=self.user1,
                                         content='content',
                                         region='N/A',
                                         category='others')
        self.comment1 = Comment.objects.create(body='test comment',
                                               commenter=self.user1,
                                               post=self.post1)


    def test_get_postlist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')


    def test_get_add_story_will_redirect_to_login_if_not_logged_in(self):
        response = self.client.get(reverse('add_story'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))
  

    def test_can_get_add_story_if_logged_in(self):
        response = self.c.get("/add_story/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html', 'add_story.html')


    def test_add_story_POST_can_add_story(self):
        response = self.c.post('/add_story/',
                               {'title': 'title2',
                                'content': 'test',
                                'region': 'N/A',
                                'category': 'others',
                                'save': 'draft'})
    
        post = Post.objects.filter(slug='title2').first()
        self.assertEqual(post.title, 'title2')
        self.assertEqual(post.content, 'test')
        self.assertRedirects(response, f'/detail/{post.slug}/')


    def test_add_story_POST_will_set_status_to_1_if_submit_clicked(self):
        response = self.c.post('/add_story/',
                                {
                                    'title': 'title2',
                                    'content': 'test',
                                    'region': 'N/A',
                                    'category': 'others',
                                    'submit': 'complete'
                                },
                              )
        post = Post.objects.filter(slug='title2').first()
        self.assertEqual(post.title, 'title2')
        self.assertEqual(post.status, 1)
        self.assertRedirects(response, f'/detail/{post.slug}/')


    def test_add_story_POST_keeps_status_to_0_if_save_clicked(self):
        response = self.c.post('/add_story/',
                               {'title': 'title2',
                                'content': 'test',
                                'region': 'N/A',
                                'category': 'others',
                                'save': 'draft'})
        post = Post.objects.filter(slug='title2').first()
        self.assertEqual(post.title, 'title2')
        self.assertEqual(post.status, 0)
        self.assertRedirects(response, f'/detail/{post.slug}/')


    # NG 
    # def test_post_add_story_empty_input_will_raise_error(self):
    #     response = self.c.post('/add_story/',
    #                             {
    #                                 'title': '',
    #                                 'content': '',
    #                                 'region': 'N/A',
    #                                 'category': 'others',
    #                                 'save': 'draft'
    #                             },
    #                           )
    #     request = response.wsgi_request
    #     print(request.messages)


    def test_add_story_POST_save_will_render_msg_draft_saved(self):
        response = self.c.post('/add_story/',
                                {'title': 'title2',
                                 'content': 'test',
                                 'region': 'N/A',
                                 'category': 'others',
                                 'save': 'draft'})
        messages = list(get_messages(response.wsgi_request))       
        self.assertEqual(str(messages[0]), 'Your draft has been saved.')

    
    def test_message_says_draft_is_submitted_if_submitted(self):
        response = self.c.post('/add_story/',
                                {'title': 'title2',
                                 'content': 'test',
                                 'region': 'N/A',
                                 'category': 'others',
                                 'submit': 'complete'})
        messages = list(get_messages(response.wsgi_request))       
        self.assertEqual(str(messages[0]),
                         'Your story has been submitted for evaluation.')


    def test_can_get_detail_page(self):
        response = self.client.get(f'/detail/{self.post1.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html', 'base.html')


    # the following 4 needs self.assertRedirects(response, f'/detail/{post.slug}/')?
    def test_post_detail_GET_liked_set_False_if_not_liked(self):
        response = self.c2.get(f'/detail/{self.post1.slug}/')
        self.assertEqual(response.context['liked'], False)


    def test_post_like_GET_will_set_liked_True_if_liked(self):
        post = Post.objects.filter(slug=self.post1.slug).first()
        post.likes.add(self.user2)
        post.save()
        self.assertTrue(post.likes.filter(id=self.user2.id).exists())
        response = self.c2.get(f'/detail/{self.post1.slug}/')
        self.assertEqual(response.context['liked'], True)


    def test_post_detail_POST_liked_set_False_if_not_liked(self):
        response = self.c2.post(f'/detail/{self.post1.slug}/')
        self.assertEqual(response.context['liked'], False)


    def test_post_like_POST_will_set_liked_True_if_liked(self):
        post = Post.objects.filter(slug=self.post1.slug).first()
        post.likes.add(self.user2)
        post.save()
        self.assertTrue(post.likes.filter(id=self.user2.id).exists())
        response = self.c2.post(f'/detail/{self.post1.slug}/')
        self.assertEqual(response.context['liked'], True)


    def test_post_detail_POST_can_post_comment(self):
        response = self.c.post(f'/detail/{self.post1.slug}/',
                               {
                                    'body': 'test comment'
                                }
                               )
        comment = Comment.objects.filter(commenter=self.user1).last()
        self.assertEqual(comment.body, 'test comment')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html', 'base.html')

    
    def test_detail_GET_will_show_update_btn_if_status_0_and_user_is_author(self):
        response = self.c.get(f'/detail/{self.post1.slug}/')
        self.assertContains(response,
                            '<button class="btn btn-submit" type="submit">Update</button>',
                            status_code=200)

    
    def test_detail_GET_will_not_show_update_btn_if_status_1(self):
        self.post1.status = 1
        self.post1.save()
        response = self.c.get(f'/detail/{self.post1.slug}/')
        self.assertNotContains(response,
                               '<button class="btn btn-submit" type="submit">Update</button>',
                               status_code=200)

                    
    def test_detail_GET_will_not_show_update_btn_if_status_2(self):
        self.post1.status = 2
        self.post1.save()
        response = self.c.get(f'/detail/{self.post1.slug}/')
        self.assertNotContains(response,
                               '<button class="btn btn-submit" type="submit">Update</button>',
                               status_code=200)

                            
    def test_detail_GET_will_not_show_update_btn_if_user_not_author(self):
        response = self.c2.get(f'/detail/{self.post1.slug}/')
        self.assertNotContains(response,
                               '<button class="btn btn-submit" type="submit">Update</button>',
                               status_code=200)


    # NG
    # def test_detail_GET_will_show_delete_btn_if_status_0_and_user_is_author(self):
    #     response = self.c.get(f'/detail/{self.post1.slug}/')
    #     self.assertContains(response,
    #                         '<button type="submit" class="btn btn-submit delete_post item-right" name="delete_post" value="{{post.slug}}">Delete</button>',
    #                         status_code=200)


    # def test_post_detail_POST_no_input_for_comment_will_prompt_input(self):
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


    # def test_post_detail_POST_spaces_for_comment_will_show_error_message(self):
    #     response = self.c.post('/detail/title1/',
    #                            {
    #                                 'body': '  '
    #                             }
    #                            )
    #     comment = Comment.objects.filter(commenter=self.user1)
    #     self.assertEqual(len(comment), 1)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'post_detail.html', 'base.html')
        # how to get error message?


    def test_post_like_POST_will_add_user(self):
        response = self.c2.post(reverse('post_like',
                                        kwargs={'slug': self.post1.slug}))
        post = Post.objects.filter(slug=self.post1.slug).first()
        self.assertRedirects(response, f'/detail/{self.post1.slug}/')
        self.assertTrue(post.likes.filter(id=self.user2.id).exists())

    
    def test_post_like_POST_for_the_second_time_will_remove_user(self):
        response = self.c2.post(reverse('post_like',
                                   kwargs={'slug': self.post1.slug}))
        response = self.c2.post(reverse('post_like',
                                   kwargs={'slug': self.post1.slug}))
        post = Post.objects.filter(slug=self.post1.slug).first()
        self.assertRedirects(response, f'/detail/{self.post1.slug}/')
        self.assertFalse(post.likes.filter(id=self.user2.id).exists())


    def test_bookmark_POST_will_add_user(self):
        response = self.c2.post(reverse('bookmark',
                                   kwargs={'slug': self.post1.slug}))
        post = Post.objects.filter(slug=self.post1.slug).first()
        self.assertRedirects(response, f'/detail/{self.post1.slug}/')
        self.assertTrue(post.bookmark.filter(id=self.user2.id).exists())


    def test_bookmark_POST_will_remove_user(self):
        response = self.c2.post(reverse('bookmark',
                                        kwargs={'slug': self.post1.slug}))
        response = self.c2.post(reverse('bookmark',
                                        kwargs={'slug': self.post1.slug}))
        post = Post.objects.filter(slug=self.post1.slug).first()
        self.assertRedirects(response, f'/detail/{self.post1.slug}/')
        self.assertFalse(post.bookmark.filter(id=self.user2.id).exists())


    def test_update_comment_GET_gets_the_page_if_right_user(self):
        response = self.c.get('/update_comment/comment1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_comment.html', 'base.html')


    def test_update_comment_GET_will_redirect_to_login_if_not_logged_in(self):
        response = self.client.get('/update_comment/comment1/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))


    def test_update_comment_GET_will_403_if_wrong_user(self):
        response = self.c2.get(reverse('update_comment', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 403)


    def test_update_comment_POST_will_update_comment(self):
        response = self.c.post('/update_comment/comment1/',
                                {'body': 'comment updated'})
        comment = Comment.objects.filter(commenter=self.user1).first()
        self.assertEqual(comment.body, 'comment updated')
        self.assertEqual(comment.comment_status, 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/detail/{comment.post.slug}/')


    def test_update_comment_POST_cancel_will_not_update_comment(self):
        response = self.c.post('/update_comment/comment1/',
                                {'body': 'comment updated',
                                 'cancel': 'cancel'})
        comment = Comment.objects.filter(commenter=self.user1).first()
        self.assertEqual(comment.body, 'test comment')
        self.assertEqual(comment.comment_status, 0)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/detail/{comment.post.slug}/')


    def test_delete_comment_POST_will_set_comment_status_to_2(self):
        response = self.c.post('/delete_comment/comment1/')
        comment = Comment.objects.filter(commenter=self.user1).first()
        self.assertEqual(comment.comment_status, 2)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/detail/{comment.post.slug}/')


    def test_update_post_GET_gets_the_page_if_right_user(self):
        response = self.c.get(f'/update/{self.post1.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_post.html', 'base.html')


    def test_update_post_GET_will_redirect_to_login_if_not_logged_in(self):
        response = self.client.get(f'/update/{self.post1.slug}/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))


    def test_update_post_GET_will_403_if_wrong_user(self):
        response = self.c2.get(f'/update/{self.post1.slug}/')
        self.assertEqual(response.status_code, 403)


    def test_update_post_GET_will_403_if_submitted(self):
        self.post1.status = 1
        self.post1.save()
        response = self.c.get(f'/update/{self.post1.slug}/')
        self.assertEqual(response.status_code, 403)


    def test_update_post_GET_will_403_if_published(self):
        self.post1.status = 2
        self.post1.save()
        response = self.c.get(f'/update/{self.post1.slug}/')
        self.assertEqual(response.status_code, 403)


    def test_update_post_POST_will_update_content(self):
        response = self.c.post(reverse('update_post',
                               kwargs={'slug': self.post1.slug}),
                               {'title': 'title1',
                                'content': 'content updated',
                                'region': 'N/A',
                                'category': 'others',
                                'save': 'draft'})
        post = Post.objects.filter(slug=self.post1.slug).first()
        self.assertEqual(post.title, 'title1')
        self.assertEqual(post.content, 'content updated')
        self.assertEqual(post.region, 'N/A')
        self.assertEqual(post.category, 'others')
        self.assertRedirects(response, f'/detail/{post.slug}/')


    def test_update_post_POST_will_update_title(self):
        response = self.c.post(reverse('update_post',
                               kwargs={'slug': self.post1.slug}),
                               {'title': 'title2',
                                'content': 'content',
                                'region': 'N/A',
                                'category': 'others',
                                'save': 'draft'})
        post = Post.objects.filter(slug=self.post1.slug).first()
        self.assertEqual(post.title, 'title2')
        self.assertEqual(post.content, 'content')
        self.assertEqual(post.region, 'N/A')
        self.assertEqual(post.category, 'others')
        self.assertRedirects(response, f'/detail/{post.slug}/')


    def test_update_post_POST_will_update_region(self):
        response = self.c.post(reverse('update_post',
                               kwargs={'slug': self.post1.slug}),
                               {'title': 'title1',
                                'content': 'content',
                                'region': 'NAM',
                                'category': 'others',
                                'save': 'draft'})
        post = Post.objects.filter(slug=self.post1.slug).first()
        self.assertEqual(post.title, 'title1')
        self.assertEqual(post.content, 'content')
        self.assertEqual(post.region, 'NAM')
        self.assertEqual(post.category, 'others')
        self.assertRedirects(response, f'/detail/{post.slug}/')


    def test_update_post_POST_will_update_category(self):
        response = self.c.post(reverse('update_post',
                               kwargs={'slug': self.post1.slug}),
                               {'title': 'title1',
                                'content': 'content',
                                'region': 'N/A',
                                'category': 'aquatic system',
                                'save': 'draft'})
        post = Post.objects.filter(slug=self.post1.slug).first()
        self.assertEqual(post.title, 'title1')
        self.assertEqual(post.content, 'content')
        self.assertEqual(post.region, 'N/A')
        self.assertEqual(post.category, 'aquatic system')
        self.assertRedirects(response, f'/detail/{post.slug}/')


    def test_update_post_POST_cancel_will_not_update_post(self):
        response = self.c.post(reverse('update_post',
                                       kwargs={'slug': self.post1.slug}),
                               {'title': 'title2',
                                'content': 'content updated',
                                'region': 'N/A',
                                'category': 'others',
                                'cancel': 'cancel'})
        post = Post.objects.filter(slug=self.post1.slug).first()
        self.assertEqual(post.title, 'title1')
        self.assertEqual(post.content, 'content')
        self.assertEqual(post.region, 'N/A')
        self.assertEqual(post.category, 'others')
        self.assertRedirects(response, f'/detail/{post.slug}/')


    def test_update_post_POST_submit_will_set_status_to_1(self):
        response = self.c.post(reverse('update_post',
                                       kwargs={'slug': self.post1.slug}),
                               {'title': 'title1',
                                'content': 'content',
                                'region': 'N/A',
                                'category': 'others',
                                'submit': 'complete'})
        post = Post.objects.filter(slug=self.post1.slug).first()
        self.assertEqual(post.status, 1)
        self.assertRedirects(response, f'/detail/{post.slug}/')


    def test_delete_post_POST_will_delete_post_if_right_user(self):
        response = self.c.post(reverse('delete_post',
                                      kwargs={'slug': self.post1.slug}))
        existing_posts = Post.objects.filter(slug=self.post1.slug)
        self.assertEqual(len(existing_posts), 0)
        self.assertRedirects(response, '/')


    def test_can_get_more_stories(self):
        response = self.client.get('/more_stories/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'more_stories.html')


    # need to test the content of object_list?
    def test_can_get_more_stories(self):
        response = self.client.get('/more_stories/')
        print(response.context['object_list'])


    def test_my_page_GET_will_get_page_if_user(self):
        response = self.c.get('/mypage/user1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_page.html', 'base.html')


    def test_my_page_GET_will_403_if_wrong_user(self):
        response = self.c2.get('/mypage/user1/')
        self.assertEqual(response.status_code, 403)


class TestSearchView(TestCase):

    def setUp(self):
        """create test posts."""
        self.user1 = User.objects.create_user(username="user1", password="pw1")
        self.user2 = User.objects.create_user(username="user2", password="pw2")
        self.user3 = User.objects.create_user(username="user3", password="pw3")
        
        self.post1 = Post.objects.create(title='gray cat',
                                         author=self.user1,
                                         content='content',
                                         region='N/A',
                                         category='others',
                                         status=2)
        self.post1.save()
        
        self.post2 = Post.objects.create(title='white cat',
                                         author=self.user2,
                                         content='content',
                                         region='N/A',
                                         category='others',
                                         status=2)
        self.post2.save()
        
        self.post3 = Post.objects.create(title='brown dog',
                                         author=self.user3,
                                         content='content',
                                         region='N/A',
                                         category='others',
                                         status=2)
        self.post3.save()


    def test_search_GET_will_get_page(self):
        response = self.client.get('/search_story/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')


    def test_category_choices_are_right(self):
        response = self.client.get('/search_story/')
        category_choices = Post._meta.get_field('category').choices
        categories = [cat[1] for cat in category_choices]
        self.assertEqual(response.context['categories'], categories)


    def test_search_clicked_set_to_True_if_search_clicked(self):
        response = self.client.get('/search_story/',
                                   {'search': 'search'})
        self.assertEqual(response.context['search_clicked'], True)


    def test_search_by_title_contains_will_get_right_posts(self):
        response = self.client.get('/search_story/',
                                   {'title_input': 'cat',
                                    'title_filter': 'contains',
                                    'category': 'Choose...',
                                    'region': 'Choose...',
                                    'search': 'search'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
        self.assertEqual(list(response.context['queryset']), [self.post2, self.post1])


    def test_search_by_title_contains_will_return_empty_queryset_if_no_match(self):
        response = self.client.get('/search_story/',
                                   {'title_input': 'rabbit',
                                    'title_filter': 'contains',
                                    'category': 'Choose...',
                                    'region': 'Choose...',
                                    'search': 'search'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
        self.assertEqual(len(response.context['queryset']), 0)


    def test_search_by_title_is_exactly_will_return_right_post_for_exact_title(self):
        response = self.client.get('/search_story/',
                                   {'title_input': 'gray cat',
                                    'title_filter': 'is_exactly',
                                    'category': 'Choose...',
                                    'region': 'Choose...',
                                    'search': 'search'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
        self.assertEqual(len(response.context['queryset']), 1)
        self.assertEqual(response.context['queryset'][0], self.post1)


    def test_search_by_title_is_exactly_will_return_empty_queryset_if_no_match(self):
        response = self.client.get('/search_story/',
                                   {'title_input': 'green cat',
                                    'title_filter': 'is_exactly',
                                    'category': 'Choose...',
                                    'region': 'Choose...',
                                    'search': 'search'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
        self.assertEqual(len(response.context['queryset']), 0)
            

if __name__ == '__main__':
    main()