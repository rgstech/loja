from django.contrib import admin

# Register your models here.
from .models import Produto




class ProdutoAdmin(admin.ModelAdmin):
    
    list_display = ("id","titulo", "desc", 
                    "preco_compra", "preco_venda", 
                    "quant", "disponivel" , "dt_cadastro")

admin.site.register(Produto, ProdutoAdmin)