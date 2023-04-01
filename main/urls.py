from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('create_article', views.CreateArticleView.as_view(), name='create_article'),
    path('detail_article/<int:pk>', views.DetailArticleView.as_view(), name='detail_article'),
    path('list_article', views.ListArticleView.as_view(), name='list_article'),
    path('news_article', views.NewsArticleView.as_view(), name='news_article'),
    path('create_test', views.CreateTestView.as_view(), name='create_test'),
]
