from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^archive$', views.archive, name="archive"),
   	url(r'^resources$', TemplateView.as_view(template_name='resources.html'), name='resources'),
    url(r'^archive/add$', views.post_new, name="post_new"),
    url(r'^search/', include('haystack.urls')),
    url(r'^(?P<plink>[a-zA-Z0-9]+)$', views.details, name="details"),
    url(r'^(?P<plink>[a-zA-Z0-9]+)/edit$', views.post_edit, name="post_edit"),
    url(r'^(?P<plink>[a-zA-Z0-9]+)/publish$', views.post_publish, name="post_publish"),
]