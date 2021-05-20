from django.contrib import admin
from .models import receita

class Listandoreceita(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'tempo_preparo')
    list_display_links = ('id', 'nome_receita')


admin.site.register(receita, Listandoreceita)
