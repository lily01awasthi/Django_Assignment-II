from django.urls import path
from .views import Register, Home, Blog, PostCreate
from django.contrib.auth import views as auth_views

app_name='blogs'
urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('blog', Blog.as_view(),name='blog_home'),
    path('register/', Register.as_view(),name='register'),
    path('post/new',PostCreate.as_view(),name='post_create'),
    path('login',auth_views.LoginView.as_view(template_name='blog/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='blog/logout.html'),name='logout'),
]
