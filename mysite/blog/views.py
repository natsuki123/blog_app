from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def HelloWorldView(request):
    return HttpResponse("<h1>ReHelloWorld!!!</h1>")