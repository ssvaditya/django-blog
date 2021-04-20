from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, AddCommentView, UserPostListView
from . import views


urlpatterns =[
        path('', PostListView.as_view(), name= 'blog-home'),
        path('user/<str:username>', UserPostListView.as_view(), name= 'user-posts'),
        path('post/<int:pk>/', PostDetailView.as_view(), name= 'post-detail'),
        path('post/new/', PostCreateView.as_view(), name='post-create'),
        path('post/<int:pk>/update/', PostUpdateView.as_view(), name= 'post-update'),
        path('post/<int:pk>/delete/', PostDeleteView.as_view(), name= 'post-delete'),
        path('post/<int:pk>/comment/', AddCommentView.as_view(), name= 'post-comment'),
        path('post/<int:pk>/like/', views.like_post, name= 'like'),
        path('about/', views.about, name= 'blog-about'),
        path('data/', views.data, name= 'blog-data'),
        path('export-user/', views.export_user, name= 'export-user'),
    ]

