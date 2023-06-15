
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Produto
from .forms import ProdutoForm


def index(request):

    produtos = Produto.objects.all()
    return render(request, 'produto.html', {'produtos': produtos,
                                            'produtoform': ProdutoForm})


def createproduto(request):
    if request.method == 'GET': #GET
        produtos = Produto.objects.all()
        return render(request, 'produto.html', {'produtos': produtos,
                                                'produtoform': ProdutoForm})
    else:  # POST
        try:
            form = ProdutoForm(request.POST)
            form.save()
            return redirect(to='produto')
        except ValueError:
            produtos = Produto.objects.all()
            return render(request, 'produto.html', {'produtos': produtos,
                                                    'produtoform': ProdutoForm,
                                                    'error': 'bad data passed in'})


def deleteproduto(request, produto_id):

    try:
        produto = get_object_or_404(Produto, pk=produto_id)
        produto.delete()

        return redirect(to='produto')
    except ValueError:
        produtos = Produto.objects.all()
        return render(request, 'produto.html', {'produtos': produtos,
                                                'produtoform': ProdutoForm,
                                                'error': 'bad data passed in'})


def editproduto(request, produto_id):  # edit and update

    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == 'GET': #GET
        form = ProdutoForm(instance=produto)
        return render(request, 'produto-edit.html', {'produto': produto,
                                                     'produtoform': form})
    else:  # POST
        try:
            form = ProdutoForm(request.POST, instance=produto)
            form.save()
            return redirect(to='produto')
        except ValueError:
            return render(request, 'produto-edit.html', {'produto': produto,
                                                         'produtoform': form,
                                                         'error': 'Bad data in form'})
