# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
from django.db.models import Q
from urllib import quote_plus
from .models import Quarto
from .forms import QuartoForm
from hospedagem.models import Hospedagem
# Create your views here.

def quartos_list(request):
    queryset_list = Quarto.objects.all().order_by("numero")
    context = {
        'queryset': queryset_list,
    }
    return render(request, 'quartos_list.html', context)

def quartos_create(request):
    form = QuartoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Quarto adicionado com sucesso!')
        return redirect('quartos:list')
    context = {
        'form': form,
    }
    return render(request, 'quartos_create.html', context)


def quartos_update(request, numero):
    obj = get_object_or_404(Quarto, numero=numero)
    form = QuartoForm(request.POST or None, instance=obj)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Quarto Atualizado!')
        return redirect('quartos:list')
    context = {
        'title': 'DETAIL',
        'object': obj,
        'form': form,
    }
    return render(request, 'quartos_create.html', context)

def quartos_delete(request, numero):
    obj = get_object_or_404(Quarto, numero=numero)
    if obj.has_hospedagem():
        messages.error(request, 'Quarto com hóspede, impossível remover agora!')
    else:
        obj.delete()
        messages.success(request, 'Quarto Removido')
    return redirect('quartos:list')