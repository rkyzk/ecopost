from .models import Post, Photo, Comment
from cloudinary.forms import CloudinaryFileField
from django import forms


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image', 'region', 'category')
        featured_image = CloudinaryFileField(
            options = {
                'tags': "directly_uploaded",
                'crop': 'fill_pad', 'width': 510, 'height': 340,
                'gravity': 'auto',
                'q_auto': 'good'
            })


        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['featured_image'].required = False


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# class PhotoForm(forms.ModelForm):

#     class Meta:
#         model = PostForm
#         fields = ('image',)

#     featured_image = CloudinaryFileField(
#         options = {
#             'tags': "directly_uploaded",
#             'crop': 'fill_pad', 'width': 510, 'height': 340,
#             'gravity': 'auto',
#             'q_auto': 'good'
#         })
   