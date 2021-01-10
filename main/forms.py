from django import forms
from .models import Article, Category

choices = Category.objects.all().values_list('name', 'name') 
choice_list = []


for item in choices:
    choice_list.append(item)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'title_tag', 'image', 'author', 'category', 'content')

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
                'category': forms.Select(choices = choice_list, attrs={'class': 'form-control'}),
                'author': forms.Select(attrs={'class': 'form-control'}),
                'content': forms.Textarea(attrs={'class': 'form-control'}),
                }


class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'title_tag', 'content')

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
                'content': forms.Textarea(attrs={'class': 'form-control'}),
                }
