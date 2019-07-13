from django.contrib import admin
from app_blog.models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','created','updated','status']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status','author','created','publish')#tuple comma most me requried for single value
    search_fields = ('title','body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish' #add navbar in show date is publish
    ordering = ['status','publish']
admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','body','created','updated','active']
    list_filter = ('created','updated','active')
    search_fields = ('name','email','body')
admin.site.register(Comment,CommentAdmin)
