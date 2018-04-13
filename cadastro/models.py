# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cadastro(models.Model):

    idCadastro = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name='Nome')
    lastName = models.CharField(max_length = 50, verbose_name = "sobrenome")
    email = models.CharField(max_length = 50, verbose_name = 'telefone')
    telephone = models.IntegerField(verbose_name='telefone')

    def __str__(self):
        return self.first_name
