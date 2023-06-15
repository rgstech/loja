from django.forms import ModelForm

from .models import Produto


class ProdutoForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        
        super(ModelForm, self).__init__(*args, **kwargs)
         
        for fieldname in ['titulo', 'desc', 'preco_compra', 'preco_venda','quant']:
            self.fields[fieldname].help_text = None #tira o texto de ajuda
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'}) #adiciona atributo class com a class do bootstrap
    
    class Meta:
        model = Produto
        fields = ('titulo',
                  'desc', 
                  'preco_compra',
                  'preco_venda',
                  'quant',
                  'disponivel')

