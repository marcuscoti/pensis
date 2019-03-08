# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Quarto

# Register your models here.
class QuartoAdmin(admin.ModelAdmin):
    class Meta:
        model = Quarto
    list_display = ('numero', 'banheiro', 'descricao')
    list_display_links = ('numero', 'descricao')
    list_editable = ['banheiro']

admin.site.register(Quarto, QuartoAdmin)