# Create your views here.
from News.models import News
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    list_of_news = News.objects.all().order_by('-published_date')[:5]
    
    context = {
        'news': list_of_news,
    }
    return render_to_response(
        'news.html',
        context,
        context_instance = RequestContext(request),)
    