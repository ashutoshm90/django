from django.conf.urls import include, url, patterns
from kuchv import settings


urlpatterns = patterns('',
                    url(r'^all/$', 'article.views.articles'),
                    url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
                    url(r'^language/(?P<language>[a-z\-]+)/$', 'article.views.language'),
                    url(r'^create/$', 'article.views.create'),
                    url(r'^like/(?P<article_id>\d+)/$', 'article.views.like_article'),
                    url(r'^add_comment/(?P<article_id>\d+)/$', 'article.views.add_comment'),
                    url(r'^search/$', 'article.views.search_titles'),
                       )
urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}), )