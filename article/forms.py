from django import forms
from article.models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = {'title', 'body', 'thumbnail'}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'firstname','lastname', 'body'}