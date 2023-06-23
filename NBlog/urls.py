from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostListView.as_view(), name='home-page'),
    path('about/', views.about, name='about'),
    path('registration/', views.register, name='registration'),
    path('user/<str:user_name>/', views.user_info, name='user-info'),
    path('bloggers/', views.BlogersListView.as_view(), name='bloggers'),
    path('profile/update', views.update_profile, name='update-profile'),
    path('blogs/', views.all_blogs, name='all-blogs'),
    path('blog/<str:blog_name>/', views.blog, name='blog-info'),
    path('create_new_blog', views.PostCreate.as_view(), name='new-blog'),
    path('update_blog/<pk>', views.PostUpdate.as_view(), name='update-blog'),
    path('delete_blog/<pk>', views.PostDelete.as_view(), name='delete-blog'),
    path('blog/update_comment/<pk>', views.CommentUpdate.as_view(), name='update-comment'),
    path('blog/delete_comment/<pk>', views.CommentDelete.as_view(), name='delete-comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
