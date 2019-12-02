from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Tracking Squirrels')

# Create your views here.
