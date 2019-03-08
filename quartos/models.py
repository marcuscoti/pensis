# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth import authenticate, get_user_model, login, logout
User = get_user_model()

# Create your models here.

class Quarto(models.Model):
    BANHEIRO_C = (
        ('COL', 'Coletivo'),
        ('COM', 'Compartilhado'),
        ('S', 'Suíte'),
    )
    numero = models.IntegerField(unique=True)
    descricao = models.CharField(max_length=30, null=True, blank=True)
    banheiro = models.CharField(max_length=3, choices=BANHEIRO_C, default='COL')

    class Meta:
        ordering = ['numero']

    def __unicode__(self):
        label = str(self.numero) + "-" + self.banheiro
        return str(self.numero)

    def __str__(self):
        label = str(self.numero) + "-" + self.banheiro
        return str(self.numero)

    def get_banheiro(self):
        for choice in Quarto.BANHEIRO_C:
            if choice[0] == self.banheiro:
                return choice[1]

    def get_descricao(self):
        if self.descricao == None:
            return "----------------"
        else:
            return self.descricao

    def has_hospede(self):
        if len(self.hospedagem_set.all()) > 0:
            return True
        else:
            return False