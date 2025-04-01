from django.urls import path
from . import views
<<<<<<< HEAD
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # Dashboard and home
    path('', views.dashboard, name='dashboard'),

    # Contact and submissions
    path('contact/', views.contact_view, name='contact'),
    path('submissions/', views.submissions_view, name='submissions'),
    path('success/', views.success_view, name='success'),

    # Blog-related URLs
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/create/', views.create_blog, name='create_blog'),
    path('blogs/delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('blogs/<int:post_id>/', views.post_detail, name='post_detail'),
    path('topics/<int:topic_id>/', views.topic_detail, name='topic_detail'),

    # User authentication
    path('login/', auth_views.LoginView.as_view(template_name='index.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('register/', csrf_exempt(views.register), name='register'),

    # Optional routes
    path('signup2/', views.signup2, name='signup2'),
    path('blog/', views.blog_view, name='blog'),
=======

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('contact/', views.contact_view, name='contact'),
    path('submissions/', views.submissions_view, name='submissions'),
    path('success/', views.success_view, name='success'),
>>>>>>> 388fceab (First commit)
]
