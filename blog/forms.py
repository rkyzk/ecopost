from .models import Post, Photo, Comment
from cloudinary.forms import CloudinaryFileField
from django import forms


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'region', 'category')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PhotoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        # self.fields['name'] = "photo_form"


    class Meta:
        model = Photo
        fields = ('image',)

    image = CloudinaryFileField(
        options = {
            'tags': "directly_uploaded",
            'crop': 'fill_pad', 'width': 510, 'height': 340,
            'gravity': 'auto',
            'q_auto': 'good'
        })