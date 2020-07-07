from django.contrib import admin, auth
from .models import ArticleCategory, Article
from django.contrib.auth import get_user_model

class ArticleAdmin(admin.ModelAdmin):

    fieldsets = [(None, {'fields': ['title', 'category', 'status', 'content']}),
                 ('常规信息', {'fields':['author', 'created_by','modified_by']}),
                 ('附加信息', {'fields': ['pub_date']}),
                 ]
    list_display = ('title', 'content', 'created_by')  # ,'modified_dt','modified_by')



# Register your models here.
admin.site.register(ArticleCategory)
admin.site.register(Article, ArticleAdmin)

