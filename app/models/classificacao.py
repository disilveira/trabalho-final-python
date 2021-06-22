from django.db import models

class ClassificacaoManager(models.Manager):
    def get_classificacoes(self):
        return self.all()

class Classificacao(models.Model):
    nomeClassificacao = models.CharField(max_length=100)
    objects = ClassificacaoManager()
