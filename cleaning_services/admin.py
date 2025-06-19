from django.contrib import admin
from .models import BlogPost, Tag, Service, Comment

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Tag)
admin.site.register(Service)
admin.site.register(Comment)