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
        

    def test_featured_flag_default_to_False(self):
        self.assertEqual(self.post1.featured_flag, False)    


    def test_published_on_can_be_blank(self): # necessary, and right?
        self.assertEqual(self.post1.published_on, None)


    def test_featured_image_default_to_placeholder(self):
        self.assertEqual(self.post1.featured_image, 'placeholder')


    # test_the_image_is_transformed


    def test_region_default_to_NA(self):
        self.assertEqual(self.post1.region, 'N/A')


    def test_category_default_to_Others(self):
        self.assertEqual(self.post1.category, 'Others')


    def test_str_method_will_return_title(self):
        self.assertEqual(str(self.post1), 'title_1')


    def test_posts_ordered_by_created_on_newest_to_oldest(self):
        posts = Post.objects.all()
        i = 0
        for i in range(len(posts) - 2):
            self.assertGreater(posts[i].created_on, posts[i+1].created_on)
            i += 1
      
    
    # def test_save_method_will_slugify_post_if_not(self):
    #     """test the newly made post6 will have slug value of none
    #        while already saved title_1 will have slug 'title_1'"""
    #     self.post6 = Post.objects.create(title="test_title_6",
    #                                      author="user_1",
    #                                      content="test sentences")
    #     assertEqual(self.post6.slug, None)
    #     assertEqual(self.post1.slug, 'title_1')

    # why fail?
    # def test_num_of_likes_count_num_of_likes(self):
    #     self.assertEqual(self.post1.number_of_likes, self.post1.likes.count())

                                    # content="test sentences")    



        

if __name__ == "__main__":
    main()