from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.Receita, name='receita'),
    path('buscar', views.Buscar_view, name='buscar'),
    path('cria/receita', views.cria_receita, name='cria_receita'),
    path('deleta/<int:receita_id>', views.deleta_receita, name='deleta_receita'),
    path('edita/<int:receita_id>', views.edita_receita, name='edita_receita'),
    path('atualiza_receita', views.atualiza_receita, name='atualiza_receita'),
]