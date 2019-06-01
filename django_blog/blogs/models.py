from django.db import models
from stdimage.models import StdImageField


# Create your models here.

class Blog(models.Model):
    title = models.CharField(blank=False, null=False, max_length=150)
    text = models.TextField(blank=True)
    #以下追加
    image = StdImageField(upload_to='blogs', blank=True, null=True, variations={
        'large': (600, 400),
        'thumbnail': (100, 100, True),
        'medium': (300, 200),
        })
    #終わり
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.title
