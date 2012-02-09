from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from photolog.models import GalleryPlugin, Gallery, GalleryShow

class CMSGalleryPlugin(CMSPluginBase):
    """
        Plugin class for the latest news
    """
    model = GalleryPlugin
    name = "Gallery List"
    render_template = "photolog/list.html"
    
    
    def render(self, context, instance, placeholder):
        """
            Render the latest data
        """
        latest = Gallery.objects.all()
        context.update({
            'instance': instance,
            'latest': latest,
            'placeholder': placeholder,
        })
        return context

class CMSGalleryShow(CMSPluginBase):
    """
        Plugin class for the latest news
    """
    model = GalleryShow
    name = "Gallery Slideshow"
    render_template = "photolog/slide.html"
    
    
    def render(self, context, instance, placeholder):
        """
            Render the latest data
        """
        context.update({
            'instance': instance,
            'photos': instance.gallery.photos.all(),
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(CMSGalleryPlugin)
plugin_pool.register_plugin(CMSGalleryShow)