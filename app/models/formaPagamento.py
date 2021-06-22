from django.db import models

class formaPagamento(models.Model):
    nomeformaPagamento = models.CharField(max_length=100)