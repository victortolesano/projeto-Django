# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Cadastro

def cadastro_novo_usuario(request):

    nome = Cadastro.objects.all()
    '''context = {'pessoa':pessoa}'''
    return render(request,'html/cadastro.html')

# Create your views here.
#subindo os arquivos para o git
