from django.contrib import admin
from .models import ArticleCategory, Article


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title', 'category', 'status', 'content']}),
                 ('附加信息', {'fields': ['pub_date']}),
                 ]
    # list_display = ('title', 'content', 'created_by')  # ,'modified_dt','modified_by')


# Register your models here.
admin.site.register(ArticleCategory)
admin.site.register(Article, ArticleAdmin)
