# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
from django.db.models import Q
from urllib import quote_plus
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hospede
from .forms import HospedeForm

# Create your views here.
class HospedeList(ListView):
    context_object_name = 'hospede_list'
    queryset = Hospede.objects.filter(ativo=True)
    template_name = 'hospedes_list.html'

class HospedeList_All(ListView):
    context_object_name = 'hospede_list'
    queryset = Hospede.objects.all()
    template_name = 'hospedes_list.html'

class HospedeList_Inactive(ListView):
    context_object_name = 'hospede_list'
    queryset = Hospede.objects.filter(ativo=False)
    template_name = 'hospedes_list.html'

class HospedeCreate(CreateView):
    model = Hospede
    form_class = HospedeForm
    template_name = 'hospede_create_form.html'

class HospedeDetail(DetailView):
    model = Hospede
    template_name = 'hospedes_detail.html'
    def get_context_data(self, **kwargs):
        context = super(HospedeDetail, self).get_context_data(**kwargs)
        return context

class HospedeUpdate(UpdateView):
    model = Hospede
    form_class = HospedeForm
    #fields = ['nome']
    template_name = 'hospede_create_form.html'

def hospedes_delete(request, pk):
    obj = get_object_or_404(Hospede, pk=pk)
    if obj.has_hospedagem():
        messages.error(request, 'Pessoa com hospedagem ativa, impossível remover agora!')
    else:
        obj.delete()
        messages.success(request, 'Hóspede Removido')
    return redirect('hospedes:list')