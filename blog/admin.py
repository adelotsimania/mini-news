from django.contrib import admin
from .models import Post, Category
from .models import Comment

admin.site.register(Post)
admin.site.register(Category)

admin.site.register(Comment)
