from django.shortcuts import render
from django. http import HttpResponse

# Create your views here.

def support(request):
    return  render(request, "Click selection to login")