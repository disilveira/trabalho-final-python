from django.db import models

class Classificacao(models.Model):
    nomeClassificacao = models.CharField(max_length=100)
