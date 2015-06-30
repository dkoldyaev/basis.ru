__author__ = 'dkoldyaev'

import os

from django import template
from django.template.defaultfilters import stringfilter
from PIL import Image

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

            masks = [
                'masks/news_image_1.png',
                'masks/news_image_2.png',
                'masks/news_image_3.png',
            ]

            import random

            image =     ImageHelper.open(image_path_without_media)
            mask =      ImageHelper.open(random.choice(masks))
            background= Image.new('RGB', mask.size, '#ffffff')

            result =    ImageHelper.fit(
                image,
                mask.size
            )

            result =    ImageHelper.mask(result, mask)
            result =    ImageHelper.put(result, background)

            result.save(save_path, 'JPEG', quality = 85, optimize=True, progressive=True)

        return save_path.replace(settings.MEDIA_ROOT, settings.MEDIA_URL)

    except:

        return image_path