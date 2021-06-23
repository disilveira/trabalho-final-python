from . import Classificacao, formaPagamento
from django.db import models

class contasReceberManager(models.Manager):
    def get_contasReceber(self):
        return self.all()

    def gerar_relatorio(self):
        return contasReceber.objects.order_by('dataExpectativa')

class contasReceber(models.Model):
    dataExpectativa = models.DateField(null=False)
    dataRecebimento = models.DateField(null=True)
    valor = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    descricao = models.TextField(null=True)
    classificacao = models.ForeignKey(Classificacao, on_delete=models.SET_NULL, null=True)
    formaPagamento = models.ForeignKey(formaPagamento, on_delete=models.SET_NULL, null=True)
    situacao = models.BooleanField(default=0)
    objects = contasReceberManager()