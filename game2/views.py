import random
from django.shortcuts import render

# Create your views here.


def game2(request): # type: ignore
    return render(request, 'game2/game2.html') # type: ignore
