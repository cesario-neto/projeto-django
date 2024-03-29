from django.http import request
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from receitas.models import receita
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    receitas = receita.objects.order_by('-data_receita').filter(publicado=True)
    paginator = Paginator(receitas, 3)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)


    dados = {
        'receitas': receitas_por_pagina
    }

    return render(request,'index.html' ,dados)

def Receita(request, receita_id):
    recipe = get_object_or_404(receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : recipe
    }

    return render(request, 'receita.html', receita_a_exibir)

def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        recipe = receita.objects.create(pessoa=user, nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria, foto_receita=foto_receita)
        recipe.save()   
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')

def deleta_receita(request, receita_id):
    recipe = get_object_or_404(receita, pk=receita_id)
    recipe.delete()
    return redirect ('dashboard')

def edita_receita(request, receita_id):
    recipe = get_object_or_404(receita, pk=receita_id)
    receita_a_edita = { 'recipe': recipe }
    return render(request, 'usuarios/edita_receita.html', receita_a_edita)

def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = receita.objects.get(pk=receita_id)
        print(receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        r.save()
        return redirect('dashboard')

