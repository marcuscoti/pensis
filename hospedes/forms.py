# -*- coding: utf-8 -*-
from django import forms
from .models import Hospede

class HospedeForm(forms.ModelForm):
    class Meta:
        model = Hospede
        exclude = ['updated', 'ativo']
        labels = {
            'user': 'Usuário',
            'nome': 'Nome',
            'email': 'E-Mail',
            'nascimento': 'Data Nascimento',
            'rg': 'RG',
            'cpf': 'CPF',
            'sexo': 'Sexo',
            'estado_civil': 'Estado Civil',
            'profissao': 'Profissão',
            'telefone': 'Telefone'
        }