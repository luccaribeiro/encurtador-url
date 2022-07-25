import requests
from django.http import HttpResponse
from django.shortcuts import render

from .forms import RegistroLink


def index(request):
    form = RegistroLink()
    return render(request, 'encurta/index.html', {'form':form})

def encurta(request): 
    form = RegistroLink(request.POST)
    url = form.data['url']
    api_key = "87cbbff44dd55c76031bc99c9085c756e41a2"
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
    data = requests.get(api_url).json()["url"]
    if data["status"] == 7:	
        shortened_url = data["shortLink"]
        form = shortened_url
    else:
        return HttpResponse("Deu Ruim")
    n = 1
    return render(request, 'encurta/resultado.html', {'form':form})
