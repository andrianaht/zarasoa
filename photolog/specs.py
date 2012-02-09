""" Default Photologue image specifications """

from imagekit.specs import ImageSpec
from imagekit import processors
    

class ResizeThumbnail(processors.Resize):
    width = 100
    height = 75
    crop = True
    
class ResizeDisplay(processors.Resize):
    width = 600
    
class EnhanceSmall(processors.Adjustment):
    contrast = 1.2
    sharpness = 1.1
    
class AdminThumbnail(ImageSpec):
    access_as = 'admin_thumbnail'
    processors = [ResizeThumbnail, EnhanceSmall]

class Display(ImageSpec):
    increment_count = True
    processors = [ResizeDisplay]
        
class Thumbnail(ImageSpec):
    processors = [ResizeThumbnail, EnhanceSmall]
    pre_cache = True
