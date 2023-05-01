from .models import Post, Comment
from django_countries.fields import CountryField
from django import forms


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image', 'city', 'country', 'category']

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['featured_image'].required = False


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': ''
        }
