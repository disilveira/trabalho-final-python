from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pessoa
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

@require_http_methods(['GET'])
def index(request):
    return HttpResponse("Trabalho Final Python - Fluxo de Caixa")