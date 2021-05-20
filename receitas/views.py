from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import receita

def index(request):

    
    receitas = receita.objects.all()

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