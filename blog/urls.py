"""This module holds url paths used in blog app."""

from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', views.PostList.as_view(), name='home'),
        path('mypage/user<int:pk>/', views.MyPage.as_view(), name='mypage'),
        path('search_stories/', views.SearchPosts.as_view(), name='search'),
        path('add_story/', views.AddStory.as_view(), name='add_story'),
        path('more_stories/', views.MoreStories.as_view(),
             name='more_stories'),
        path('popular_stories/', views.PopularStories.as_view(),
             name='popular_stories'),
        path('update/<slug:slug>/', views.UpdatePost.as_view(),
             name='update_post'),
        path('delete/<slug:slug>/', views.DeletePost.as_view(),
             name='delete_post'),
        path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
        path('bookmark/<slug:slug>/', views.Bookmark.as_view(),
             name='bookmark'),
        path('update_comment/comment<int:id>/', views.UpdateComment.as_view(),
             name='update_comment'),
        path('delete_comment/comment<int:id>/', views.DeleteComment.as_view(),
             name='delete_comment'),
        path('detail/<slug:slug>/', views.PostDetail.as_view(),
             name='detail_page')
]
