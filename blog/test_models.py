from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from sqlite3 import IntegrityError
from .models import Post, Comment


class TestPostModels(TestCase):

    def setUp(self):
        """create test users and posts"""
        self.user_1 = User.objects.create(username="test1", password="password")
        self.user_2 = User.objects.create(username="test2", password="password")      
        self.post1 = Post.objects.create(
            title="title_1",
            author=self.user_1,
            content="test sentences"
            )
        self.post2 = Post.objects.create(
            title="title_2",
            author=self.user_2,
            content="test 2 sentences"
            )


    def test_two_posts_cannot_have_the_same_title(self):                                         
        with self.assertRaises(Exception) as raised:
            Post.objects.create(title="title_1", author=self.user_2,
                                content="test sentences", category='others',
                                region='N/A')
        self.assertTrue(IntegrityError, type(raised.exception))
    

    def test_featured_flag_default_to_False(self):
        self.assertEqual(self.post1.featured_flag, False)


    def test_featured_image_default_to_placeholder(self):
        self.assertEqual(self.post1.featured_image, 'placeholder')


    # test_the_image_is_transformed


    def test_region_default_to_NA(self):
        self.assertEqual(self.post1.region, 'N/A')


    def test_category_default_to_Others(self):
        self.assertEqual(self.post1.category, 'Others')


    def test_posts_ordered_by_created_on_newest_to_oldest(self):
        posts = Post.objects.all()
        i = 0
        for i in range(len(posts) - 2):
            self.assertGreater(posts[i].created_on, posts[i+1].created_on)
            i += 1
      
    # how to test save method specifically? Can I prevent save method and see if it doesn't slugify?
    def test_save_method_will_slugify_post(self):
        self.assertEqual(self.post1.slug, 'title_1')


    def test_str_method_will_return_title(self):
        self.assertEqual(str(self.post1), 'title_1')


    def test_num_of_likes_count_num_of_likes(self):
        self.post1.likes.add(self.user_2)
        self.assertEqual(self.post1.number_of_likes(),
                         self.post1.likes.count())


    def test_pub_date_returns_string_message_if_not_published(self):
        self.assertEqual(self.post2.pub_date(), 'Not published')


    def test_pub_date_returns_specified_format_if_published(self):
        date = datetime.utcnow()
        self.post1.status = 2
        self.post1.published_on = date
        self.assertEqual(self.post1.pub_date(), date.strftime("%B %d, %Y"))


    # def test_excerpt_returns_specified_str(self):
    #     content = "I'm writing a long content to test " + \
    #         "if the excerpt method returns the first 199 characters and " + \
    #         "... are returned. test test test test test sentences." + \
    #         "test sentences, test sentences, test sentences, " + \
    #         "test sentences, test sentences, test sentences."
    #     post3 = Post.objects.create(
    #         title="title_3",
    #         author=self.user_1,
    #         content=content
    #     )
    #     self.assertEqual(post3.excerpt(), content)


    # def test_get_absolute_url(self):


class TestCommentModels(TestCase):

    def setUp(self):
        """create test users and posts"""
        self.user_1 = User.objects.create(username="test1", password="password")
        self.user_2 = User.objects.create(username="test2", password="password")      
        self.post1 = Post.objects.create(
            title="title_1",
            author=self.user_1,
            content="test sentences"
            )
        self.comment1 = Comment.objects.create(
            commenter=self.user_1,
            post=self.post1,
            body='test comment'
        )

    
    def test_comment_status_default_to_0(self):
        self.assertEqual(self.comment1.comment_status, 0)


    def test_comments_ordered_from_oldest_to_newest(self):
        comment2 = Comment.objects.create(
            commenter=self.user_1,
            post=self.post1,
            body='2nd test comment'
        )
        comments = Comment.objects.all()
        i = 0
        for i in range(len(comments) - 2):
            self.assertLess(comments[i].created_on, comments[i+1].created_on)
            i += 1


    def test_str_method_will_return_body_and_commenter(self):
        self.assertEqual(str(self.comment1), 'test comment by test1')


if __name__ == "__main__":
    main()