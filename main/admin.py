from django.contrib import admin
from .models import Article, Chat, Test

# Register your models here.
admin.site.register(Article)
admin.site.register(Chat)
admin.site.register(Test)