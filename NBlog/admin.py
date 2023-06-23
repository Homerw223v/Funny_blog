from django.contrib import admin
from .models import Comment, Post, Bloger


# Register your models here.


@admin.register(Comment)
class CommentInLine(admin.ModelAdmin):
    fields = ['post', 'author', 'comment']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'description', 'author', 'post_date']


@admin.register(Bloger)
class BlogerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'bloger_bio', 'genre']
