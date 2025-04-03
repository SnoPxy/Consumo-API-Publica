from django.shortcuts import render
import requests

# Create your views here.


def main(request):
    return render(request,'main .html')

def pegar_api():
    url = "https://dados.tcerj.tc.br/api/v1/compras_diretas_municipio"
    response = requests.get(url) 
    return response.json()

def consulta_processos(request):
    dados = pegar_api()
    
    if isinstance(dados, list):
        dados = {"Compras": dados}
    return render(request, "main.html", {"dadosProcessos": dados})

