
from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    
        path('', views.home, name='home'),
        path('teste/', HomePageView.as_view(), name='teste'),
]
