from django.urls import path
from . import views

urlpatterns = [
    path('', views.consulta_processos, name='consulta_processos'),
]
