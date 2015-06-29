# -*- coding: utf-8 -*-
__author__ = 'dkoldyaev'

from django.utils.safestring import mark_safe
from django.forms import widgets
from django.db.models.fields.files import ImageFieldFile, FieldFile

from basis.templatetags.admin_preview import admin_preview
from basis.templatetags.image_helper import ImageHelper

class ImageWidget(widgets.ClearableFileInput) :

    def render(self, name, value, attrs=None):

        sizes = (attrs.pop('width', 300), attrs.pop('height', 150))
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        template_parts = []

        image_preview = ''

        if value and isinstance(value, ImageFieldFile) and hasattr(value, "url") :

            try:
                image_preview_src = admin_preview(value.url, sizes)
                image_preview = u'<img src="{image_preview_src}" style="float:left; margin:0 1em 1em 0;" />'.format(image_preview_src=image_preview_src)
            except:
                image_preview = u'<img src="{image_preview_src}" style="float:left; margin:0 1em 1em 0;" />'.format(image_preview_src=u'/static/img/error.png')

            try :
                image = ImageHelper.open(value.url)
                image_name = value.url.split('/')[-1]

            except:
                image = None
                image_name = u'<span style="color:red; font-weight:bold;">неправильное имя файла</span>'

            original_info = u'''

                    <dt>Оригинал</dt>
                    <dd><a href="{image_src}" target="_blank">{image_name}</a> ({image_size_x}px, {image_size_y}px)</dd>

            '''.format(
                image_src =     value.url,
                image_name =    image_name,
                image_size_x =  image.size[0] if image is not None else 0,
                image_size_y =  image.size[1] if image is not None else 0
            )

            template_parts.append(original_info)

            if not self.is_required :

                checkbox_name = self.clear_checkbox_name(name)
                checkbox_id = self.clear_checkbox_id(checkbox_name)
                checkbox = widgets.CheckboxInput().render(checkbox_name, False, attrs={'id': checkbox_id})

                delete_info = u'''

                    <dt>Удалить</dt>
                    <dd>{delete_checkbox}</dd>

                '''.format(delete_checkbox=checkbox)

                template_parts.append(delete_info)

        upload_info = u'''

            <dt>Изменить</dt>
            <dd><input id="{input_id}" name="{input_name}" type="file"></dd>

        '''.format(input_id=final_attrs.get('id'), input_name=final_attrs.get('name'))

        template_parts.append(upload_info)

        template = u'''

            {image_preview}

            <div style="display:block; overflow:hidden; min-width: 100px;">
                <dl>

                {template_parts}

                </dl>
            </div>

        '''.format(
            image_preview=image_preview,
            template_parts=''.join(template_parts),
            **final_attrs
        )

        return mark_safe(template)

class SVGImageWidget(widgets.ClearableFileInput):

    background_image = False

    def __init__(self, *args, **kwargs):

        self.background_image = kwargs.pop('background_image', False)

        super(SVGImageWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):

        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        template_parts = []

        image_preview = ''

        if value and isinstance(value, FieldFile) and hasattr(value, "url") :

            image_preview_src = value.url
            if self.background_image :
                image_preview = u'<img src="{image_preview_src}" ' \
                                u'style="float:left; margin:0 1em 1em 0; background:url({background_image})" />'.format(image_preview_src=image_preview_src, background_image=self.background_image)
            else:
                image_preview = u'<img src="{image_preview_src}" style="float:left; margin:0 1em 1em 0;" />'.format(image_preview_src=image_preview_src)

            image_name = value.url.split('/')[-1]

            original_info = u'''

                    <dt>Оригинал</dt>
                    <dd><a href="{image_src}" target="_blank">{image_name}</a></dd>

            '''.format(
                image_src =     value.url,
                image_name =    image_name
            )

            template_parts.append(original_info)

            if not self.is_required :

                checkbox_name = self.clear_checkbox_name(name)
                checkbox_id = self.clear_checkbox_id(checkbox_name)
                checkbox = widgets.CheckboxInput().render(checkbox_name, False, attrs={'id': checkbox_id})

                delete_info = u'''

                    <dt>Удалить</dt>
                    <dd>{delete_checkbox}</dd>

                '''.format(delete_checkbox=checkbox)

                template_parts.append(delete_info)

        upload_info = u'''

            <dt>Изменить</dt>
            <dd><input id="{input_id}" name="{input_name}" type="file"></dd>

        '''.format(input_id=final_attrs.get('id'), input_name=final_attrs.get('name'))

        template_parts.append(upload_info)

        template = u'''

            {image_preview}

            <div style="display:block; overflow:hidden; min-width: 100px;">
                <dl>

                {template_parts}

                </dl>
            </div>

        '''.format(
            image_preview=image_preview,
            template_parts=''.join(template_parts),
            **final_attrs
        )

        return mark_safe(template)

class CheckboxWithPreviewWidget(widgets.CheckboxSelectMultiple):

    @classmethod
    def get_image_urls(cls):

        return {}

    def render(self, name, value, attrs=None, choices=()):

        if len(choices) == 0 :

            choices = [c for c in self.choices]

        if len(choices) == 0 :

            return super(CheckboxWithPreviewWidget, self).render(name, value, attrs=attrs, choices=choices)

        image_urls = self.get_image_urls()

        rendered_choices = map(
            lambda choice:u'<li class="checkox_with_previews_list_item {checked_class}">'
                          u'<input  type="checkbox" '
                          u'        value="{checkbox_value}"'\
                          u'        name="{checkbox_name}" '\
                          u'        id="{checkbox_id}" '\
                          u'        class="{checkbox_class}"'\
                          u'        {checked} />'
                          u'<label class="checkbox_with_preview" for="{checkbox_id}">'\
                          u'     <img src="{preview_src}" class="checkbox_with_preview__preview" />'\
                          u'     <br/>'\
                          u'     {label_text}'\
                          u'</label>'
                          u'</li>'\
            .format(
                checkbox_value= choice[0],
                checkbox_name = name,
                checkbox_class= u'checkbox_with_preview_' + name,
                checkbox_id =   u'%s_%d' % (name, choice[0]),
                preview_src =   image_urls.get(choice[0], '/noimage_path.png'),
                label_text =    choice[1],
                checked =       u'checked="checked"' if value is not None and choice[0] in value else u'',
                checked_class = u'checkox_with_previews_list_item__checked' if value is not None and choice[0] in value else u''
            ),
            choices
        )

        all_choice =    u' <label class="checkbox_with_preview_all" for="{checkbox_id}">'\
                        u'     <input  type="checkbox" '\
                        u'             name="{checkbox_name}" '\
                        u'             id="{checkbox_id}" '\
                        u'             class="{checkbox_class}"' \
                        u'             {checked} />'\
                        u'     {label_text}'\
                        u'</label>'\
            .format(
                checkbox_name = name + u'_all',
                checkbox_class= u'checkbox_with_preview_' + name,
                checkbox_id =   u'_'.join([name, 'all']),
                label_text =    u'Отметить все',
                checked =       u'checked="checked"' if value is not None and len(value) == len(choices) else u''
            )

        all_choice_script = u'  <script type="text/javascript">' \
                            u'      $(document).ready(function(){{' \
                            u'          $("#{checkbox_id}").change(function(){{' \
                            u'              $(".{checkbox_class}").not("#{checkbox_id}").prop("checked", $(this).prop("checked"));' \
                            u'              ' \
                            u'              if ($(this).prop("checked")) {{' \
                            u'                  $(".{checkbox_class}").not("#{checkbox_id}").parents(".checkox_with_previews_list_item").addClass("checkox_with_previews_list_item__checked")' \
                            u'              }} else {{' \
                            u'                  $(".{checkbox_class}").not("#{checkbox_id}").parents(".checkox_with_previews_list_item").removeClass("checkox_with_previews_list_item__checked")' \
                            u'              }}' \
                            u'          }});' \
                            u'          $(".{checkbox_class}").not("#{checkbox_id}").change(function(){{' \
                            u'              if ($(".{checkbox_class}").not("#{checkbox_id}").not(":checked").size()==0) {{' \
                            u'                  $("#{checkbox_id}").prop("checked", true)' \
                            u'              }} else {{' \
                            u'                  $("#{checkbox_id}").prop("checked", false)' \
                            u'              }}' \
                            u'              ' \
                            u'              if ($(this).is(":checked")) {{' \
                            u'                  $(this).parents(".checkox_with_previews_list_item").addClass("checkox_with_previews_list_item__checked")' \
                            u'              }} else {{' \
                            u'                  $(this).parents(".checkox_with_previews_list_item").removeClass("checkox_with_previews_list_item__checked")' \
                            u'              }}' \
                            u'          }})' \
                            u'      }})' \
                            u'  </script>'\
            .format(
                checkbox_id=    u'_'.join([name, 'all']),
                checkbox_class= u'checkbox_with_preview_' + name
            )

        return mark_safe(
            u'<div class="checkox_with_previews_all">'+\
                all_choice + \
            u'</div>' +\
            all_choice_script + \
            u'<ul class="checkox_with_previews_list">' + u''.join(rendered_choices) + u'</ul>'
        )