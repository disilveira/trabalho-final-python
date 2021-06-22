from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Classificacao, formaPagamento, contasPagar, contasReceber

class classificacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classificacao
        fields = ('id', 'nomeClassificacao')