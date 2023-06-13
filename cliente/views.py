
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm


def index(request):

    clientes = Cliente.objects.all()
    return render(request, 'cliente.html', {'clientes': clientes,
                                            'clienteform': ClienteForm})


def createcliente(request):
    if request.method == 'GET': #GET
        clientes = Cliente.objects.all()
        return render(request, 'cliente.html', {'clientes': clientes,
                                                'clienteform': ClienteForm})
    else:  # POST
        try:
            form = ClienteForm(request.POST)
            form.save()
            return redirect(to='cliente')
        except ValueError:
            clientes = Cliente.objects.all()
            return render(request, 'cliente.html', {'clientes': clientes,
                                                    'clienteform': ClienteForm,
                                                    'error': 'bad data passed in'})


def deletecliente(request, cliente_id):

    try:
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        cliente.delete()

        return redirect(to='cliente')
    except ValueError:
        clientes = Cliente.objects.all()
        return render(request, 'cliente.html', {'clientes': clientes,
                                                'clienteform': ClienteForm,
                                                'error': 'bad data passed in'})


def editcliente(request, cliente_id):  # edit and update

    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'GET': #GET
        form = ClienteForm(instance=cliente)
        return render(request, 'cliente-edit.html', {'cliente': cliente,
                                                     'clienteform': form})
    else:  # POST
        try:
            form = ClienteForm(request.POST, instance=cliente)
            form.save()
            return redirect(to='cliente')
        except ValueError:
            return render(request, 'cliente-edit.html', {'cliente': cliente,
                                                         'clienteform': form,
                                                         'error': 'Bad data in form'})
