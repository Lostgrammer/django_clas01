from django.shortcuts import render
#importamos el http response
from django.http import HttpResponse

# las vistas retornan html
def  index(request):
    return HttpResponse('Hola a todos')

def  hello(request):
    return HttpResponse('Hola')
