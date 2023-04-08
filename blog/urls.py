from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', views.PostList.as_view(), name='home'),
        path('add_story/', views.AddStory.as_view(), name='add_story'),
        path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]