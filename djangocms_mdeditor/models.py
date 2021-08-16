# coding: utf-8
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import strip_tags
from django.utils.text import Truncator
from cms.models import CMSPlugin
from martor.models import MartorField
from martor.utils import markdownify
from .fields import MarkdownFormField


class MarkdownField(MartorField):
    """
    Extend martor.models.MartorField to provide CSS-fix media-field.
    """
    def formfield(self, **kwargs):
        defaults = {'form_class': MarkdownFormField}
        defaults.update(kwargs)
        return super(MarkdownField, self).formfield(**defaults)


class MarkdownText(CMSPlugin):
    """
    Markdown Text Plugin Class.
    """
    body = MarkdownField(_('body'),)

    def __str__(self):
        return Truncator(strip_tags(markdownify(self.body)).replace(
            '&shy;', '')).words(3, truncate="...")
