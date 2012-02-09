from django import template
from photolog.models import Gallery
register = template.Library()

@register.inclusion_tag('photolog/tags/next_in_gallery.html')
def next_in_gallery(photo, gallery):
    return {'photo': photo.get_next_in_gallery(gallery)}

@register.inclusion_tag('photolog/tags/prev_in_gallery.html')
def previous_in_gallery(photo, gallery):
    return {'photo': photo.get_previous_in_gallery(gallery)}

def get_thumbnails(var, arg):
    return var.get_thumbnails(arg)

def get_thumbnail_picture(var):
    return var.get_thumbnail()

register.filter('get_thumbnails', get_thumbnails)
register.filter('get_thumbnail_picture', get_thumbnail_picture)

