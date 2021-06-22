from rest_framework import viewsets
from .serializers import classificacaoSerializer, contasPagarSerializer, contasReceberSerializer, formaPagamentoSerializer
from .models import Classificacao, formaPagamento, contasPagar, contasReceber

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