from . import Classificacao, formaPagamento
from django.db import models
from django.db.models import Sum

class contasReceberManager(models.Manager):
    def get_contasReceber(self):
        return self.all()

    def gerar_relatorio(self):
        return contasReceber.objects.order_by('dataExpectativa')

    def obter_somaPrevisto_mes(self, i):
        soma = float(contasReceber.objects.filter(dataExpectativa__month=i, situacao=False).aggregate(Sum('valor'))['valor__sum'] or 0)
        return soma

    def obter_somaRealizado_mes(self, i):
        soma = float(contasReceber.objects.filter(dataExpectativa__month=i, situacao=True).aggregate(Sum('valor'))['valor__sum'] or 0)
        return soma

    def obter_soma_mes(self, i):
        soma = float(contasReceber.objects.filter(dataExpectativa__month=i).aggregate(Sum('valor'))['valor__sum'] or 0)
        return soma

    def obter_ganhos_classificacao(self, i):

        ganhos = []

        for x in range (1,19):
            soma = float(contasReceber.objects.filter(dataExpectativa__month=i, classificacao=x).aggregate(Sum('valor'))['valor__sum'] or 0)
            ganho = {
            'classificacao' : Classificacao.objects.obter_classificacao_id(x),
            'soma' : soma
            }
            if soma > 0:
                ganhos.append(ganho)
        return ganhos

class contasReceber(models.Model):
    dataExpectativa = models.DateField(null=False)
    dataRecebimento = models.DateField(null=True)
    valor = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    descricao = models.TextField(null=True)
    classificacao = models.ForeignKey(Classificacao, on_delete=models.SET_NULL, null=True)
    formaPagamento = models.ForeignKey(formaPagamento, on_delete=models.SET_NULL, null=True)
    situacao = models.BooleanField(default=0)
    objects = contasReceberManager()