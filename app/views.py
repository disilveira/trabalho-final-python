from rest_framework import viewsets
from .serializers import classificacaoSerializer
from .models import Classificacao

class classificacaoViewSet(viewsets.ModelViewSet):
    queryset = Classificacao.objects.all()
    serializer_class = classificacaoSerializer