from django.shortcuts import render, redirect



def index(request) -> None:
    return render(request, 'index.html')