# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    clientevenda = models.TextField(max_length=255, null=True, blank=True)
    valor = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Cliente(models.Model):

    #__Cliente_FIELDS__
    nome = models.TextField(max_length=255, null=True, blank=True)
    telefone = models.TextField(max_length=255, null=True, blank=True)
    ativo = models.BooleanField()
    data_cadastro = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Cliente_FIELDS__END

    class Meta:
        verbose_name        = _("Cliente")
        verbose_name_plural = _("Cliente")


class Vendas(models.Model):

    #__Vendas_FIELDS__
    data = models.DateTimeField(blank=True, null=True, default=timezone.now)
    cliente = models.TextField(max_length=255, null=True, blank=True)
    telefone = models.TextField(max_length=255, null=True, blank=True)

    #__Vendas_FIELDS__END

    class Meta:
        verbose_name        = _("Vendas")
        verbose_name_plural = _("Vendas")



#__MODELS__END
