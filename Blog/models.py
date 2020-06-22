from django.db import models
from mdeditor.fields import  MDTextField

# Create your models here.
class Article(models.Model):
    title = models.CharField('This is article title',max_length=100)
    pub_date = models.DateTimeField('article publish date time')
    content = MDTextField()


