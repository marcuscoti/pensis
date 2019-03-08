# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Hospede

# Register your models here.
class HospedeAdmin(admin.ModelAdmin):
    class Meta:
        model = Hospede
    list_display = ('nome', 'email', 'telefone', 'user')
    list_display_links = ('nome', 'email', 'telefone', 'user')
    list_filter = ('nome', 'email')
    #list_editable = ['title']
    search_fields = ['nome', 'email']

admin.site.register(Hospede, HospedeAdmin)
