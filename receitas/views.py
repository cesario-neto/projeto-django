from django.http import request
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import receita

def index(request):
    receitas = receita.objects.order_by('-data_receita').filter(publicado=True)

    dados = {
        'receitas': receitas
    }

    return render(request,'index.html' ,dados)

def Receita(request, receita_id):
    recipe = get_object_or_404(receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : recipe
    }

    return render(request, 'receita.html', receita_a_exibir)

def Buscar_view (request):
    lista_receitas = receita.objects.order_by('-data_receita').filter(publicado=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'buscar.html', dados)

