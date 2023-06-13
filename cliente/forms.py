from django.forms import ModelForm

from .models import Cliente


class ClienteForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        
        super(ModelForm, self).__init__(*args, **kwargs)
        
        for fieldname in ['nome', 'email']:
            self.fields[fieldname].help_text = None #tira o texto de ajuda
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'}) #adiciona atributo class com a class do bootstrap
    
    class Meta:
        model = Cliente
        fields = ('nome','email')

