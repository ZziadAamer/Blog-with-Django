# from django.urls import path
from django.urls import re_path
from . import views


app_name= 'post'

urlpatterns = [
    re_path(r'^$', views.all_posts, name='all_posts'),
    re_path(r'^(?P<id>\d+)$', views.post, name='post'),
    re_path(r'^create_post$', views.create_post, name='create_post'),
    re_path(r'^(?P<id>\d+)/edit$', views.edit_post, name='edit_post'),

]