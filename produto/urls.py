from django.urls import path
from . import views as produtoViews

urlpatterns = [
    path('produto/',                        produtoViews.index,         name="produto"),
    path('produto/create',                  produtoViews.createproduto, name="createproduto"),
    path('produto/delete/<int:produto_id>', produtoViews.deleteproduto, name="deleteproduto"),
    path('produto/edit/<int:produto_id>'  , produtoViews.editproduto,   name="editproduto"),
   

]
 