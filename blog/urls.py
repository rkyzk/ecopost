from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', views.PostList.as_view(), name='home'),
        path('add_story/', views.AddStory.as_view(), name='add_story'),  
        path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
        path('<slug:slug>/update/', views.UpdatePost.as_view(), name='update_post'),
        path('<slug:slug>/delete/', views.DeletePost.as_view(), name='delete_post'), 
        path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
        path('<slug:slug>/like/', views.PostLike.as_view(), name='post_like'),
        path('<slug:slug>/bookmark/', views.Bookmark.as_view(), name='bookmark'),
        path('mypage/<int:id>/', views.MyPage.as_view(), name='my_page'),      
        path('update_comment/<int:id>', views.UpdateComment.as_view(), name='update_comment'),
        path('search/', views.Search.as_view(), name='search'),
]