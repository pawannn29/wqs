from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
from graphos.sources.model import ModelDataSource
from graphos.renderers import flot

# Create your views here.
def configuration(request, ph, temperature, dissolved_oxygen):
    data = Data()
    data.ph = ph
    data.temperature = temperature
    data.dissolved_oxygen = dissolved_oxygen
    data.save()
    return HttpResponse("<h1> Data Successfully Saved </h1>")


def plot(request):
    context = {
    'instances' : Data.objects.all()
    }

    return render(request, 'plot.html', context)
def graph(request):
    context = {
        'temp':Data.objects.all()
    }   

    return render(request, 'graph.html', context)
def eg(request):
    context = {
        'temp':Data.objects.all()
    }   
    return render(request,'eg.html')    