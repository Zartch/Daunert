from django.shortcuts import render
from mantenimiento.models import Tiket, Cliente, Etiqueta
from django.contrib import messages as notif_messages

def login(request):

    return render(request,'login.html',{})



# Create your views here.
def nuevo_tiquet(request):
    # todo decidir quien eres
    # tikets = Tiket.objects.filter(usuario = usuario)
    clientes = Cliente.objects.all()

    if request.POST:
        cliente = request.POST.get('cliente')
        nombret = request.POST.get('nombret')
        desc = request.POST.get('desc')
        prioridad = request.POST.get('prioridad')
        tipo = request.POST.get('tipo')
        # etiquetas = request.POST.get_list('tags')

        # tiquet = Tiket.objects.create(tipologia = tipo, prioridad=prioridad,
        #                      cliente_id = cliente, descripcion=desc )

        # for etiqueta in etiquetas:
        #     #todo comprobar si la etiqueta es nueva, si no crear
        #     tiquet.add(Etiqueta.objects.get(id=etiqueta))

        notif_messages.add_message(request, notif_messages.INFO, "Has creat un nou Tiket", 'success')

    return render(request, 'mantenimiento/nuevo_tiquet.html', {'var1': 'Hola 6000E'})


def listado_tiquets(request):
    # tikets = Tiket.objects.filter(usuario = usuario)
    tiquets = Tiket.objects.all()

    return render(request, 'listado_t.html', {'lista':tiquets})
