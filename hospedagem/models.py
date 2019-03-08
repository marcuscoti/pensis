# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth import authenticate, get_user_model, login, logout
from quartos.models import Quarto
from hospedes.models import Hospede

User = get_user_model()

class Hospedagem(models.Model):
    hospede = models.ForeignKey(Hospede, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    entrada = models.DateField(default=timezone.now)
    proximo_vencimento = models.DateField()
    dia_vencimento = models.IntegerField()
    valor = models.IntegerField()
    observacao = models.CharField(max_length=90, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Hospedagem"
