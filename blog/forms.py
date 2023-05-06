"""This module holds forms used in ecopost."""

from .models import Post, Comment, CATEGORY
from django_countries.fields import CountryField
from django import forms


class PostForm(forms.ModelForm):
    """Form for posts."""

    class Meta:
        """Features of PostForm."""
        model = Post
        fields = ['title', 'content', 'featured_image',
                  'city', 'country', 'category']
        title = forms.CharField(required=True)
        content = forms.CharField(required=True)
        city = forms.CharField(required=True)
        country = CountryField(blank_label="(select country)")

        def __init__(self, *args, **kwargs):
            """Set required flag of featured image to False."""
            self.fields['featured_image'].required = False
            super(PostForm, self).__init__(*args, **kwargs)


class NoSpacesField(forms.CharField):

    def validate(self, value):
        # if value.replace()
        pass

class CommentForm(forms.ModelForm):
    """Form for comments."""
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': ''}
