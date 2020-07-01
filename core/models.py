from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta


# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length = 100)
    descricao = models.TextField(blank = True, null = True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateField(auto_now = True,verbose_name='Data da criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # .cascade - se o usuario for excluido, todos os...



    class Meta:
        db_table = 'evento'
    #retorna o titulo do evento no setup (senao ficará apenas a referência a um objeto)
    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False

