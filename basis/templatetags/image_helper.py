__author__ = 'dkoldyaev'

import os
from django.conf import settings

from PIL import Image

class ImageHelper:

    @staticmethod
    def tryAnimated(image):
        try:
            image.seek(1)
        except EOFError:
            return False
        else:
            return True

    @staticmethod
    def put_on_transparent(image, size, resize_image=False):
        background = Image.new('RGBA', size, (0,0,0,0))
        if resize_image:
            image = ImageHelper.thumb(image, background.size)

        background.paste(
            image.copy(),
            (
                (background.size[0] - image.size[0])/2,
                (background.size[1] - image.size[1])/2,
            )
        )

        return background

    @staticmethod
    def put(image, background, resize_image=False):
        if resize_image:
            image = ImageHelper.thumb(image, background.size)

        background.paste(
            image.copy(),
            (
                (background.size[0] - image.size[0])/2,
                (background.size[1] - image.size[1])/2,
            )
        )

        return background

    @staticmethod
    def thumb(image, thumb_size, resize=Image.ANTIALIAS):
        image_copy = image.copy()
        image_copy.thumbnail(thumb_size, resize)
        return image_copy

    @staticmethod
    def fit(image, image_size, centering=(0.5, 0.5)):
        from PIL import ImageOps
        result = ImageOps.fit(image.copy(), image_size, centering=centering)
        return result

    @staticmethod
    def mask(image, mask):
        result = image.copy()
        result = Image.alpha_composite(result.convert('RGBA'), mask.convert('RGBA'))
        return result

    @staticmethod
    def compsite(image, mask, background):
        return Image.composite(
            image,
            background,
            mask
        )

    @staticmethod
    def open(image_path):
        try:
            return Image.open(os.path.join(settings.MEDIA_ROOT, image_path))
        except:
            return Image.open(os.path.join(settings.STATIC_ROOT, image_path))

    @staticmethod
    def makedirs(path, exist_ok=False):
        sub_path = os.path.dirname(path)
        if not os.path.exists(sub_path):
            try:    ImageHelper.makedirs(sub_path)
            except: pass
        if not os.path.exists(path):
            try:    os.makedirs(path)
            except: pass

    @staticmethod
    def try_exsist_or_create_dir(image_path_without_media, action_name, format='PNG'):
        save_dir = '/'.join(settings.MEDIA_ROOT.split('/') + image_path_without_media.split('/')[0:-1] + ['cache', action_name])
        save_path = '/'.join(settings.MEDIA_ROOT.split('/') + image_path_without_media.split('/')[0:-1] + ['cache', action_name, image_path_without_media.split('/')[-1]]) + '.' + format.lower()

        save_path = save_path.replace('//', '/')
        save_dir = save_dir.replace('//', '/')

        if os.path.isfile(save_path) and not settings.DEBUG:
            return save_path, True
        if not os.path.isdir(save_dir):
            os.makedirs(save_dir)
        return save_path, False