from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html' , { "nome": "Rodrigo",
                                            'current_path': request.get_full_path() })