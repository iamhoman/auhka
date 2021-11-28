from django.contrib import admin
from .models import Post, Post_isLike, Post_comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Post_isLike)
class Post_isLike_Admin(admin.ModelAdmin):
    list_display = ('liker','created','post')


@admin.register(Post_comment)
class Post_comment_Admin(admin.ModelAdmin):
    list_display = ('commenter','created','comment')
