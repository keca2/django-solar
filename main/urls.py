from django.urls import path
from .views import ArticleDetail, AddArticle, UpdateArticle, DeleteArticle, AddCategory, Category, CategoryList
from . import views

# from .views import Home

urlpatterns = [
    #path('', Home.as_view(), name='home'),
    path('', views.HomeView, name='home'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article-detail'),
    path('add_article/', AddArticle.as_view(), name='add-article'),
    path('article/edit/<int:pk>', UpdateArticle.as_view(), name='update-article'),
    path('article/<int:pk>/delete', DeleteArticle.as_view(), name='delete-article'),
    path('add_category/', AddCategory.as_view(), name='add-category'),
    path('category/<str:cats>/', CategoryList, name='category'),
]

