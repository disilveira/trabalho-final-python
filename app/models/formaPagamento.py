from django.db import models

class formaPagamentoManager(models.Manager):
    def get_formas_pagamentos(self):
        return self.all()

class formaPagamento(models.Model):
    nomeformaPagamento = models.CharField(max_length=100)
    objects = formaPagamentoManager()

    def __str__(self):
        return f"{self.nomeformaPagamento}"