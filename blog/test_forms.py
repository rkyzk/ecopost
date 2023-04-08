from django.test import TestCase
from django.contrib.auth.models import User
from .forms import PostForm


# class TestPostForm(TestCase):

    # def test_Post_title_is_required(self):
    #     """Test if the title is required for 'Post' model."""
    #     user = User.objects.create(username='test',

    #                                password='password')
    #     form = PostForm({
    #         'title': '',
    #         'author': user,
    #         'content': 'content'
    #     })
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('title', form.error.keys())
    #     self.assertEqual(form.errors['title'][0], 'This field is required.')