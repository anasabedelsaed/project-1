from django.shortcuts import render  # type: ignore
import random

# Create your views here.


def game1(request):  # type: ignore
    return render(request, 'game1/game1.html') # type: ignore

def home(request): # type: ignore
    return render(request,'home.html') # type: ignore