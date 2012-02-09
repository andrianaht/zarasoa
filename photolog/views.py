# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from photolog.models import Gallery, Photo
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from lib.decorators import render_to
from projects.models import Project


def gallery_all(request):
	return  render_to_response('photolog/list.html', {
		'latest': Gallery.objects.filter(is_public=True),
	}, context_instance=RequestContext(request))
	
def gallery_detail(request, slug):
	gallery = Gallery.objects.get(title_slug=slug)
	return  render_to_response('photolog/gallery.html', {
		'photos': gallery.get_pictures(slug),
		'title': gallery.title,
		'date_published': gallery.date_added,
		'description': gallery.description,
	}, context_instance=RequestContext(request))
								

