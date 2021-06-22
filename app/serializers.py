from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Classificacao, formaPagamento, contasPagar, contasReceber

class classificacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classificacao
        fields = ('id', 'nomeClassificacao')

class formaPagamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = formaPagamento
        fields = ('id', 'nomeformaPagamento')

class contasPagarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = contasPagar
        fields = ('id', 'dataVencimento', 'dataPagamento', 'valor', 'descricao', 'classificacao', 'formaPagamento', 'situacao')

class contasReceberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = contasReceber
        fields = ('id', 'dataExpectativa', 'dataRecebimento', 'valor', 'descricao', 'classificacao', 'formaPagamento', 'situacao')