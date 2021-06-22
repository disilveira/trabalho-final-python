from . import Classificacao, formaPagamento
from django.db import models

class contasPagar(models.Model):
    dataVencimento = models.DateField(null=False)
    dataPagamento = models.DateField(null=True)
    valor = models.DecimalField(null=False, decimal_places=2)
    descricao = models.TextField(null=True)
    classificacao = models.ForeignKey(Classificacao, on_delete=models.SET_NULL, null=True)
    formaPagamento = models.ForeignKey(formaPagamento, on_delete=models.SET_NULL, null=True)
    situacao = models.BooleanField(default=0)