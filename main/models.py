from django.db import models
from django.utils import timezone
from .consts import *

# 追々はこれらのカテゴリーもモデル化したい

class Article(models.Model):
  create_date = models.DateTimeField(default=timezone.now)
  title = models.CharField(max_length=100)
  content = models.TextField()
  category = models.CharField(
    max_length=100,
    choices=ARTICLE_CATEGORY,
  )
  access_count = models.IntegerField(default=0)
  thumbnail = models.ImageField(null=True, blank=True)
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

  def __str__(self):
    return self.title

# Create your models here.
class Chat(models.Model):
  time = models.DateTimeField(default=timezone.now)
  content = models.CharField(max_length=200)
  icon = models.IntegerField()
  # icon はhtmlで表示する際、iconIDによって表示する画像を変える。
  # つまり、予め選択できるアイコンはこちらで3種類程用意しておく。
  color = models.CharField(
    max_length=7,
    choices=COLOR_VARIATION,
    )
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

  def __str__(self):
    return self.content

class Test(models.Model):
  name = models.CharField(max_length=10)
  age = models.IntegerField(default=20)