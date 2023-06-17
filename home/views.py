from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


def home(request):
    return render(request, 'home.html')
    
    
class HomePageView(TemplateView):
    template_name = "teste.html"