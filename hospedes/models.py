# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()

# Create your models here.
class Hospede(models.Model):
    ESTADO_C = (
        ('S', 'Solteiro(a)'),
        ('C', 'Casado(a)'),
        ('D', 'Divorciado(a)'),
        ('V', 'Viúvo(a)'),
    )

    SEXO_C = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    nascimento = models.DateField()
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1, default='M', choices=SEXO_C)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_C)
    profissao = models.CharField(max_length=120)
    telefone = models.CharField(max_length=120)
    ativo = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('HospedeDetail', kwargs={'pk': self.pk})

    def has_hospedagem(self):
        if len(self.hospedagem_set.all()) > 0:
            return True
        else:
            return False
