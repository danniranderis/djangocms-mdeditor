# coding: utf-8
from django.contrib import admin
from .widgets import AdminMarkdownWidget
from .models import MarkdownField


class MarkdownModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        MarkdownField: {'widget': AdminMarkdownWidget}
    }
