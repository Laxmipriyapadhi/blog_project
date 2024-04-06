from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('login/',user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('blog-detail/<int:pk>/',blog_detail,name='blog_detail'),
    path('create-blog/', create_blog, name='create_blog'),
    path('update-blog/<int:pk>/', update_blog, name='update_blog'),
    path('delete-blog/<int:pk>/',delete_blog, name='delete_blog'),
]