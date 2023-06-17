 
from django.urls import path
from . import views as clienteViews


  
urlpatterns = [
    path('cliente/',                        clienteViews.index,         name="cliente"),
    path('cliente/create',                  clienteViews.createcliente, name="createcliente"),
    path('cliente/delete/<int:cliente_id>', clienteViews.deletecliente, name="deletecliente"),
    path('cliente/edit/<int:cliente_id>'  , clienteViews.editcliente,   name="editcliente"),
   

]
 