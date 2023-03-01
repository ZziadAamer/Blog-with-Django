from django.contrib import admin
from . models import Post
# Register your models here.



class post_admin(admin.ModelAdmin) :
    list_filter= ['date']
    search_fields= ['title', 'content']
    list_display= ['title', 'date', 'active']



admin.site.register(Post, post_admin)
