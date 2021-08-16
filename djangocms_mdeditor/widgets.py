# coding: utf-8
from django.contrib.admin import widgets
from martor.widgets import MartorWidget


class MarkdownWidget(MartorWidget):
    """
    Extend of martor.widgets.MartorWidget() to incorporate extra css-files.
    """
    class Media:
        css = {'all': ('css/ace-djangocms-fix.min.css',)}


class AdminMarkdownWidget(MarkdownWidget, widgets.AdminTextareaWidget):
    pass
