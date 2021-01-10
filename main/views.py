from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Category
from .forms import ArticleForm, EditArticleForm
from django.urls import reverse_lazy


def CategoryList(request, cats):
    category_articles = Article.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.replace('-', ' '), 'category_articles':category_articles})

def HomeView(request):
    articles = Article.objects.all()
    
    context = {
            'articles': articles,
            }

    return render(request, 'home.html', context)

#class Home(ListView):
#    model = Article
#    template_name = 'home.html'
#    ordering = ['-article_date']

class ArticleDetail(DetailView):
    model = Article
    template_name = 'article-detail.html'

class AddArticle(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'add-article.html'

class UpdateArticle(UpdateView):
    model = Article
    form_class = EditArticleForm
    template_name = 'update-article.html'

class DeleteArticle(DeleteView):
    model = Article
    template_name = 'delete-article.html'
    success_url = reverse_lazy('home')

class AddCategory(CreateView):
    model = Category
    template_name = 'add-category.html'
    fields = '__all__'
