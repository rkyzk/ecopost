from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', views.PostList.as_view(), name='home'),
        path('mypage/user<int:pk>/', views.MyPage.as_view(), name='mypage'),
        path('search_story/', views.Search.as_view(), name='search'),
        path('add_story/', views.AddStory.as_view(), name='add_story'),
        path('more_stories/', views.MoreStories.as_view(), name='more_stories'),
        path('update/post<int:pk>/', views.UpdatePost.as_view(), name='update_post'),
        path('delete/post<int:pk>/', views.DeletePost.as_view(), name='delete_post'), 
        path('like/post<int:pk>/', views.PostLike.as_view(), name='post_like'),
        path('bookmark/post<int:pk>', views.Bookmark.as_view(), name='bookmark'),        
        path('update_comment/comment<int:id>/', views.UpdateComment.as_view(), name='update_comment'),
        path('delete_comment/comment<int:id>/', views.DeleteComment.as_view(), name='delete_comment'),
        path('detail/post<int:pk>/', views.PostDetail.as_view(), name='detail_page')
]