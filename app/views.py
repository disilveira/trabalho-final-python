from rest_framework import viewsets
from .serializers import classificacaoSerializer, contasPagarSerializer, contasReceberSerializer, formaPagamentoSerializer
from .models import Classificacao, formaPagamento, contasPagar, contasReceber
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import datetime

class classificacaoViewSet(viewsets.ModelViewSet):
    queryset = Classificacao.objects.all()
    serializer_class = classificacaoSerializer

class formaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = formaPagamento.objects.all()
    serializer_class = formaPagamentoSerializer

class contasPagarViewSet(viewsets.ModelViewSet):
    queryset = contasPagar.objects.all()
    serializer_class = contasPagarSerializer

class contasReceberViewSet(viewsets.ModelViewSet):
    queryset = contasReceber.objects.all()
    serializer_class = contasReceberSerializer

@require_http_methods(['GET'])
def exibir_relatorios(request):

    listaContasPagar = contasPagar.objects.gerar_relatorio()
    listaContasReceber = contasReceber.objects.gerar_relatorio()

    return render(request, 'relatorios.html', {'listaContasPagar' : listaContasPagar, 'listaContasReceber' : listaContasReceber})

@require_http_methods(['GET'])
def exibir_fluxo(request):

    meses = []

    for i in range(1, 7):

        saldo_inicial = 10000 if i == 1 else mes['saldo_final']       

        saldo_final = round(saldo_inicial - contasPagar.objects.obter_soma_mes(i) + contasReceber.objects.obter_soma_mes(i), 2)

        lucro = round(saldo_final - saldo_inicial, 2)

        mes = {
            "data" : datetime.date(1900, i, 1).strftime('%B'),
            "saldo_inicial" : saldo_inicial,
            "pagar" : {
                "somaPrevisto": contasPagar.objects.obter_somaPrevisto_mes(i),
                "somaRealizado": contasPagar.objects.obter_somaRealizado_mes(i),
                "somaMensal": contasPagar.objects.obter_soma_mes(i),
                "gastosClassificacao": contasPagar.objects.obter_gastos_classificacao(i),
            },
            "receber" : {
                "somaPrevisto": contasReceber.objects.obter_somaPrevisto_mes(i),
                "somaRecebido": contasReceber.objects.obter_somaRealizado_mes(i),
                "somaMensal": contasReceber.objects.obter_soma_mes(i),
                "ganhosClassificacao": contasReceber.objects.obter_ganhos_classificacao(i),
            },
            "saldo_final" : saldo_final,
            "lucro": lucro
        } 
        meses.append(mes)

    return render(request, 'fluxo.html', {"meses" : meses})