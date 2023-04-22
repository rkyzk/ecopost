from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.shortcuts import reverse
from cloudinary.models import CloudinaryField
import random, string


STATUS = ((0, "Draft"), (1, "Submitted"), (2, "Published"), (3, "Declined"))

COMMENT_STATUS = ((0, "original"), (1, "edited"), (2, "deleted"))

REGION = (('N/A', 'N/A'),
          ('NAM', 'North America'),
          ('CAM', 'Central America'),
          ('CRB', 'Caribbean'),
          ('SAM', 'South America'),
          ('NEU', 'Northern Europe'),
          ('WEU', 'Western Europe'),
          ('EEU', 'Eastern Europe'),
          ('SEU', 'Southern Europe'),
          ('NAF', 'North Africa'),
          ('WAF', 'Western Africa'),
          ('MAF', 'Middle Africa'),
          ('EAF', 'Eastern Africa'),
          ('SAF', 'Southern Africa'),
          ('WAS', 'Western Asia'),
          ('CAS', 'Central Asia'),
          ('EAS', 'Eastern Asia'),
          ('SAS', 'Southern Asia'),
          ('SAS', 'Southeastern Asia'),
          ('ANZ', 'Australia and New Zealand'),
          ('PIS', 'Pacific Islands'))

CATEGORY = (('animals', 'Protecting animals'),
            ('aquatic system', 'Protecting the aquatic system'),
            ('saving soil & trees', 'Protecting soil & trees'),
            ('saving resources', 'Saving resources'),
            ('eco-conscious diet', 'Eco-conscious diet'),
            ('others', 'Others'))


class Post(models.Model):
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    featured_flag = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    published_on = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    featured_image = CloudinaryField('image',
                                     default='placeholder',
                                     blank=True,
                                     transformation={
                                        'crop': 'fill_pad',
                                        'width': 510,
                                        'height': 340,
                                        'gravity': 'auto',
                                        'q_auto': 'good'
                                     })
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User,
                                   related_name='post_likes',
                                   blank=True)
    region = models.CharField(max_length=30, choices=REGION, default='N/A')
    category = models.CharField(max_length=30, choices=CATEGORY,
                                default='Others')
    bookmark = models.ManyToManyField(User, related_name='bookmarked',
                                      blank=True)


    class Meta:
        ordering = ['-created_on']


    def save(self, *args, **kwargs):
        letters = string.ascii_letters
        text = ''.join(random.choice(letters) for i in range(16))
        if not self.slug:
            self.slug = slugify(self.title) + text
        super().save(*args, **kwargs)

    # 52 characters

        
    def __str__(self):
        return self.title


    def number_of_likes(self):
        return self.likes.count()


    def pub_date(self):
        if self.status == 2:
            return self.published_on.strftime("%B %d, %Y")
        else:
            return 'Not published'


    def excerpt(self):
        excerpt = str(self.content)[0:199] + "..."
        return excerpt


    def get_absolute_url(self):
        return reverse('detail_page', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='commenter')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    comment_status = models.IntegerField(choices=COMMENT_STATUS, default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.body} by {self.commenter.username}"


