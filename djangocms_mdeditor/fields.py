# coding: utf-8
from martor.fields import MartorFormField
from .widgets import MarkdownWidget


class MarkdownFormField(MartorFormField):
    """
    Extend martor.fields.MartorFormField to provide CSS-fix media-field.
    """
    def __init__(self, *args, **kwargs):
        super(MarkdownFormField, self).__init__(*args, **kwargs)
        if not issubclass(self.widget.__class__, MarkdownWidget):
            self.widget = MarkdownWidget()
