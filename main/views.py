from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,logout
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  DeleteView,
  UpdateView,
  TemplateView,
  )
from django.urls import reverse_lazy, reverse

from .models import Article, Chat, Test
from .consts import *
from .form import *

app_name = 'main'

# Create your views here.
class MainView(ListView):
  template_name = 'main/index.html'
  model = Article

class CreateArticleView(LoginRequiredMixin, CreateView):
  template_name = 'main/create_view.html'
  model = Article
  fields = ('title', 'content', 'category', 'user')
  # form_class = CreateForm
  success_url = reverse_lazy('index')

  def get_context_data(self, *args, **kwargs):
    ctx = super().get_context_data(*args, **kwargs)
    category_name_list = ARTICLE_CATEGORY
    ctx["category"] = category_name_list
    return ctx

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class DetailArticleView(DeleteView):
  template_name = 'main/detail_view.html'
  model = Article

  def get_object(self):
    q = Article.objects.get(pk=self.kwargs["pk"])
    q.access_count = q.access_count + 1
    q.save()
    return q

class ListArticleView(ListView):
  template_name = 'main/list_view.html'
  model = Article

class NewsArticleView(ListView):
  template_name = 'main/news_view.html'
  model = Article

class CreateTestView(LoginRequiredMixin, CreateView):
  template_name = 'main/create_test.html'
  model = Test
  fields = ('name',)
  success_url = reverse_lazy('index')
