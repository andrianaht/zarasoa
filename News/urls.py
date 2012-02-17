from django.conf.urls.defaults import patterns, include, url
from News import views



urlpatterns = patterns('',
    
    url(r'^$', views.index, name='news page'),
    url(r'^(?P<News_id>\d+)/$', views.news, name='details news page'),
    
    )
    
