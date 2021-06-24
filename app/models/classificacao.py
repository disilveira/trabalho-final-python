from django.db import models

class ClassificacaoManager(models.Manager):
    def get_classificacoes(self):
        return self.all()

    def obter_classificacao_id(self, id):
        return self.get(id=id)

class Classificacao(models.Model):
    nomeClassificacao = models.CharField(max_length=100)
    objects = ClassificacaoManager()

    def __str__(self):
        return f"{self.nomeClassificacao}"