from django.contrib import admin

from .models import *
admin.site.register(classificacao)
admin.site.register(formaPagamento)
admin.site.register(contasPagar)
admin.site.register(contasReceber)
