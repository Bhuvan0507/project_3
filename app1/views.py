from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def kings(request):
    return HttpResponse('we are kings')
