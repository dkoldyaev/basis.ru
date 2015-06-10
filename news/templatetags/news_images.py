__author__ = 'dkoldyaev'
from django import template
from django.template.defaultfilters import stringfilter

from basis.templatetags.image_helper import ImageHelper

register = template.Library()

@register.filter(name='news_image_fit')
@stringfilter
def news_image_fit(image_path):

    try :

        from django.conf import settings

        image_path_without_media = image_path.replace(settings.MEDIA_URL, '')

        save_path, image_is_exsist = ImageHelper.try_exsist_or_create_dir(
            image_path_without_media,
            'news_image_fit',
            format='JPEG')

        if not image_is_exsist or settings.DEBUG:

            image =     ImageHelper.open(image_path_without_media)

            result =    ImageHelper.fit(
                image,
                (800, 600)
            )

            result.save(save_path, 'JPEG', quality = 85, optimize=True, progressive=True)

        return save_path.replace(settings.MEDIA_ROOT, settings.MEDIA_URL)

    except:

        return image_path