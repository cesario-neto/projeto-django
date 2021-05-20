from django.db import models
from django.db.models.base import ModelState
from datetime import datetime
from pessoas.models import Pessoa

class receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    foto_receita = models.ImageField(upload_to ='fotos/%d,%m,%Y', blank=True)
    publicado = models.BooleanField(default=False)