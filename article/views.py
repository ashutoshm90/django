import logging

from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone
from article.models import Comment
from article.models import Article
from kuchv import settings
from article.forms import ArticleForm, CommentForm
from django.template import RequestContext
from django.contrib import messages

#from haystack.query import SearchQuerySet

logr = logging.getLogger(__name__)

# Create your views here.
def articles(request):
    language = 'en-us'
    session_language = 'en-us'
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']
    args = {}
    args.update(csrf(request))
    args['articles'] = Article.objects.all()
    args['language'] = language
    args['session_language'] = session_language
    return render_to_response('articles.html', args)

def article(request, article_id=1):
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id)}, context_instance=RequestContext(request))

def language(request, language='en-us'):
    response = HttpResponse("setting language to %s" %language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return response

def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            c = form.save(commit=False)
            c.pub_date = timezone.now()
            c.save()
            messages.add_message(request, messages.SUCCESS, "Your article was added")
            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('create_article.html', args)

def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        a.likes += 1
        a.save()
    return HttpResponseRedirect('/articles/get/%s' % article_id)

def add_comment(request, article_id):
    a = Article.objects.get(id=article_id)
    if request.method == 'POST':
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()
            messages.success(request, "Your Comment was Added")
            return HttpResponseRedirect('/articles/get/%s' % article_id)
    else:
        f = CommentForm()
    args = {}
    args.update(csrf(request))
    args['article'] = a
    args['form'] = f
    return render_to_response('add_comment.html', args)

def delete_comment(request, comment_id):
    c = Comment.objects.get(id=comment_id)
    article_id = c.article.id
    c.delete()
    messages.add_message(request, settings.DELETE_MESSAGE, "Your comment was deleted")
    return HttpResponseRedirect('/articles/get/%s' %article_id)

def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ""
    articles = Article.objects.filter(title__contains=search_text)
    return render_to_response('ajax_search.html', {'articles': articles })
