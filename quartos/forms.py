# -*- coding: utf-8 -*-
from django import forms
from .models import Quarto

class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        fields = ['numero', 'banheiro', 'descricao']
        labels = {
            'numero': 'Número',
            'banheiro': 'Banheiro',
            'descricao': 'Descrição'
        }