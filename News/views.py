# Create your views here.
from News.models import News
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse



def index(request):
    #list_of_news = News.objects.all().order_by('-published_date')[:5]
    # There is no need to filter because of ordering = "[-publised_date]" in models.Meta()
    # return the first 5 latest news
    list_of_news = News.objects.all()[:5]
    
    context = {
        'news': list_of_news,
        'SITE_DOMAIN': settings.SITE_DOMAIN,
        'ImageURL' :  'http://localhost:8000/media/',
    }
    return render_to_response(
        'news/news.html',
        context,
        context_instance = RequestContext(request),)
    
def news(request, News_id):
    new = get_object_or_404(News, pk=News_id)
        
    return render_to_response(
        'news/news_details.html',
        {'new': new},
        context_instance = RequestContext(request),        
    )
    