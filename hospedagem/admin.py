# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Hospedagem

# Register your models here.
class HospedagemAdmin(admin.ModelAdmin):
    class Meta:
        model = Hospedagem
    list_display = ('quarto', 'hospede', 'dia_vencimento', 'proximo_vencimento', 'valor')
    list_display_links = ('quarto', 'hospede', 'dia_vencimento', 'proximo_vencimento', 'valor')
    #list_filter = ('nome', 'email')
    #list_editable = ['title']
    #search_fields = ['nome', 'email']

admin.site.register(Hospedagem, HospedagemAdmin)