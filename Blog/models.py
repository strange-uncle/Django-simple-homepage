from django.db import models
from mdeditor.fields import  MDTextField
import datetime
from django.utils import timezone


# Create your models here.
PUB_STATUS = (
        ('RELEASED', '已公开发布'),
        ('DRAFT', '草稿箱'),
        ('SECRET', '仅管理员可见'),
    )

# define the basic columns for every table
# Django will setup the PK by default, don't need to handle it by myself
class BaseTableModel(models.Model):
    created_dt = models.DateTimeField('创建时间', default=timezone.now)
    created_by = models.CharField('创建人员', default='system', max_length=50)
    modified_dt = models.DateTimeField('修改时间', default=timezone.now)
    modified_by = models.CharField('修改人员', default='system', max_length=50)

    class Meta:
        # means won't generate a table for this model
        abstract = True

class ArticleCategory(BaseTableModel):
    category_name = models.CharField('文章分类',max_length=100)
    parent_category_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '分类管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category_name


class Article(BaseTableModel):
    title = models.CharField('文章标题',max_length=100)
    pub_date = models.DateTimeField('发布日期')
    status = models.CharField('发布状态',choices=PUB_STATUS, max_length=10, default='DRAFT')
    content = MDTextField('正文')
    category = models.ForeignKey(ArticleCategory, null=True, default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
