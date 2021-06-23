from django.db import router
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'classificacoes', views.classificacaoViewSet)
router.register(r'formasPagamento', views.formaPagamentoViewSet)
router.register(r'contasReceber', views.contasReceberViewSet)
router.register(r'contasPagar', views.contasPagarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('exibir_relatorios', views.exibir_relatorios, name='exibir_relatorios'),
    path('exibir_fluxo', views.exibir_fluxo, name='exibir_fluxo')
]