from django.contrib import admin
from core.models import Evento

# Register your models here.

#mostra as características do "Evento" (classe model) no setup
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','data_evento','data_criacao')
    list_filter = ('titulo','data_evento',)#filter recebe uma tupla, se for item unico colocar virgula!



admin.site.register(Evento, EventoAdmin)