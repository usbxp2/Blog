from django.contrib import admin
from app.models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','last_login','is_superuser')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','description','category','user','click_count','recommend')
    list_editable = ('category','recommend')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','index')
    list_editable = ('index',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','user','publish_date','content')


class LinksAdmin(admin.ModelAdmin):
    list_display = ('name','description','url','publish_date','index')
    list_editable = ('name','description','index')
class AdAdmin(admin.ModelAdmin):
    list_display = ('title','description','image_url','url','publish_date','index','adtype')
    list_editable = ('adtype',)



admin.site.register(User,UserAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Links,LinksAdmin)
admin.site.register(Ad,AdAdmin)