from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class BlogUser(AbstractUser):
    nick_name = models.CharField('昵称', null=False, max_length=50)
