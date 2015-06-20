
"""kuchv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from kuchv.forms import ContactForm1, ContactForm2, ContactForm3
from kuchv.views import ContactWizard
from kuchv import settings

admin.autodiscover()
urlpatterns = patterns('',
                       (r'^articles/', include('article.urls')),
                       (r'^accounts/', include('userprofile.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       #user auth urls
                       url(r'^accounts/login/$', 'kuchv.views.login'),
                       url(r'^accounts/auth/$', 'kuchv.views.auth_view'),
                       url(r'^accounts/logout/$', 'kuchv.views.logout'),
                       url(r'^accounts/loggedin/$', 'kuchv.views.loggedin'),
                       url(r'^accounts/invalid/$', 'kuchv.views.invalid_login'),
                       url(r'^accounts/register/$', 'kuchv.views.register_user'),
                       url(r'^accounts/register_success/$', 'kuchv.views.register_success'),
                       url(r'^contact/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),
                       #url(r'^search/', include('haystack.urls')),
                       url(r'^celery_test/', 'kuchv.views.start_celery_task'),
                       url(r'^celery_progress/', 'kuchv.views.monitor_celery_task')
                       )
if not settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
