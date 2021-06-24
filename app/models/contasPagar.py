from django.db.models.aggregates import Count
from . import Classificacao, formaPagamento
from django.db import models
from django.db.models import Sum

class contasPagarManager(models.Manager):
    def get_contasPagar(self):
        return self.all()

    def gerar_relatorio(self):
        return contasPagar.objects.order_by('dataVencimento')

    def obter_somaPrevisto_mes(self, i):
        soma = float(contasPagar.objects.filter(dataVencimento__month=i, situacao=False).aggregate(Sum('valor'))['valor__sum'] or 0)
        return soma

    def obter_somaRealizado_mes(self, i):
        soma = float(contasPagar.objects.filter(dataVencimento__month=i, situacao=True).aggregate(Sum('valor'))['valor__sum'] or 0)
        return soma

    def obter_soma_mes(self, i):
        soma = float(contasPagar.objects.filter(dataVencimento__month=i).aggregate(Sum('valor'))['valor__sum'] or 0)
        return soma


class contasPagar(models.Model):
    dataVencimento = models.DateField(null=False)
    dataPagamento = models.DateField(null=True)
    valor = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    descricao = models.TextField(null=True)
    classificacao = models.ForeignKey(Classificacao, on_delete=models.SET_NULL, null=True)
    formaPagamento = models.ForeignKey(formaPagamento, on_delete=models.SET_NULL, null=True)
    situacao = models.BooleanField(default=0)
    objects = contasPagarManager()