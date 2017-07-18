from django.shortcuts import render
from django.http import HttpResponse
from.models import Piano

def index(request):
    return HttpResponse('Returning this object - Welcome to Great Piano Service!')

