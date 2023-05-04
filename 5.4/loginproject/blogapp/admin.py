from django.contrib import admin
from blogapp.models import Post,	Comment
# Register your models here.
class CommentInline(admin.TabularInline):
    model	= Comment
    
@admin.register(Post)	
class PostAdmin(admin.ModelAdmin):
    list_display = ['id',	'title',	'author',	'content']
    list_display_links = ['id',	'title']
    list_filter = ['author']	
    search_fields = ['title',	'author']
    inlines = [CommentInline, 
               ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id',	'post',	'content',	'author')