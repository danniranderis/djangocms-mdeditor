# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _
from .models import MarkdownText


@plugin_pool.register_plugin
class MarkdownPluginPublisher(CMSPluginBase):
    model = MarkdownText
    module = _("Texts")
    name = _("Markdown Text")
    render_template = "render_text_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
