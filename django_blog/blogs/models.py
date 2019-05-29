from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(blank=False, null=False, max_length=150)
    text = models.TextField(blank=True)
    #以下追加
    image = models.ImageField(upload_to='blogs')
    #終わり
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.title
