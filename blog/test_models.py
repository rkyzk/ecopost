from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class TestModels(TestCase):

    def setUp(self):  # done before each test is done
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
        self.post3 = Post.objects.filter(
            title="title_3",
            author=self.user_1,
            content="test sentences"
            )


    # def test_two_posts_cannot_have_the_same_title(self):
    #     self.post5 = Post.objects.create(title="title_1",
    #                                      author=self.user_2,
    #                                      content="test sentences")
    #     self.assertRaises(IntegrityError, 'UNIQUE constraint failed')
        # sqlite3.IntegrityError: UNIQUE constraint failed: blog_post.slug


    def test_featured_flag_default_to_False(self):
        self.assertEqual(self.post1.featured_flag, False)    
        
    
    # def test_featured_flag_default_to_False(self):
    #     assertEqual(self.post1.featured_flag, False)

    # def test_posts_ordered_from_newest_to_oldest(self):
    #     i = 1
    #     for post in range(len(queryset) - 1):
    #         post.published_on > queryset[1].publisehd_on

    # def test_save_method_will_slugify_post_if_not(self):
    #     """test the newly made post6 will have slug value of none
    #        while already saved title_1 will have slug 'title_1'"""
    #     self.post6 = Post.objects.create(title="test_title_6",
    #                                      author="user_1",
    #                                      content="test sentences")
    #     assertEqual(self.post6.slug, None)
    #     assertEqual(self.post1.slug, 'title_1')

    def test_str_method_will_return_title(self):
        self.assertEqual(str(self.post1), 'title_1')

    
    # why fail?
    # def test_num_of_likes_count_num_of_likes(self):
    #     self.assertEqual(self.post1.number_of_likes, self.post1.likes.count())
        

if __name__ == "__main__":
    main()