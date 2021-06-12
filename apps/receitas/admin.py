from django.contrib import admin
from .models import receita

class Listandoreceita(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'tempo_preparo', 'categoria', 'publicado')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicado',)
    list_per_page = (6)

admin.site.register(receita, Listandoreceita)
