from django.shortcuts import render
from .models import Article, ArticleCategory
from django.views import generic

# Create your views here.
class BlogHomeView(generic.ListView):
    model = Article
    template_name = 'Blog/index.html'
    context_object_name = 'homepage_article_list'

    def get_queryset(self):
        return Article.objects.filter(status='RELEASED').order_by('-modified_dt')


class BlogDetails(generic.DetailView):
    model = Article
    template_name = 'Blog/details.html'

    def get_queryset(self):
        return Article.objects
