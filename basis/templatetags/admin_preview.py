__author__ = 'dkoldyaev'

from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

from basis.templatetags.image_helper import ImageHelper

@register.filter(name='admin_preview')
@stringfilter
def admin_preview(image_url, size=(300,150)):

    try:

        from django.conf import settings
        import os

        image_format = 'PNG'

        image_path_in_media = image_url.replace(settings.MEDIA_URL, '')

        save_path, directory_is_created = ImageHelper.try_exsist_or_create_dir(image_path_in_media, 'admin_preview', image_format)

        image = ImageHelper.open(image_path_in_media)
        image = ImageHelper.thumb(image, size)
        image.save(save_path, image_format, quality=85)

        return save_path.replace(settings.MEDIA_ROOT, settings.MEDIA_URL)

    except:

        return image_url