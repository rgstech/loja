from django.db import models

# Create your models here.



class Produto(models.Model): # model Cliente

    titulo       = models.CharField(max_length=50)
    desc         = models.TextField()
    preco_compra = models.FloatField()
    preco_venda  = models.FloatField()
    quant        = models.IntegerField()
    disponivel   = models.BooleanField()
    dt_cadastro  = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.titulo

