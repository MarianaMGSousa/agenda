from django.shortcuts import render, HttpResponse, redirect
from .models import Evento

# Create your views here.
def evento(request, titulo_evento):
    consulta = evento.objects.get(titulo=titulo_evento)#os parametros do evento titulo
    return HttpResponse('<h1>O evento será: {}</h1>'.format(consulta))

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario) #colocando um oarametro para a listagem, só vai aparecer a agenda de quem estiver logado
    dados = {'eventos' :evento}
    return render(request, 'agenda.html', dados)

# def index(request): #se não colocarmos nada será redirecionado para o /agenda
#     return redirect('/agenda/')