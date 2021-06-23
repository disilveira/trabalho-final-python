from rest_framework import viewsets
from .serializers import classificacaoSerializer, contasPagarSerializer, contasReceberSerializer, formaPagamentoSerializer
from .models import Classificacao, formaPagamento, contasPagar, contasReceber
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

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


    return render(request, 'fluxo.html')