from django.db import models

# Create your models here.


class Cliente(models.Model): # model Cliente
    nome  = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

