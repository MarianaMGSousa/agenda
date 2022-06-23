from django.contrib import admin
from .models import Evento

class EventoAdmin(admin.ModelAdmin): #para que apareça a data do evento além do título
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento')

admin.site.register(Evento, EventoAdmin)