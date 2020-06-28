from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length = 100)
    descricao = models.TextField(blank = True, null = True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento') #verboso name serve para customizar os nomes...
    #... do DjangoAdmin
    data_criacao = models.DateField(auto_now = True,verbose_name='Data da criação')
    #chave estrangeira para multusuário
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # .cascade - se o usuario for excluido, todos os...
    #... eventos dele desaparecem

    #serve para dar um nome a tabela que será criada
    class Meta:
        db_table = 'evento'
    #retorna o titulo do evento no setup (senao ficará apenas a referência a um objeto)
    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')

