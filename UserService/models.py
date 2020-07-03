from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class BlogUser(AbstractUser):
    nick_name = models.CharField('昵称', null=False, max_length=50, unique=True)
    def __str__(self):
        #use nick name to display
        #username is very sensitive and shouldn't show on page
        return self.nick_name

