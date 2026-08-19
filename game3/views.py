from django.shortcuts import render, redirect # type: ignore


# Create your views here.


def game3(request):  # type: ignore
    return render(request, 'game3/game3.html')  # type: ignore

