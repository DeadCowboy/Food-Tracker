from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"Scanner/index_scanner.html")

# Create your views here.
def addItems(requrest):
    return HttpResponse('Add items page')

def removeItems(request):
    return HttpResponse('Remvoe Items page')