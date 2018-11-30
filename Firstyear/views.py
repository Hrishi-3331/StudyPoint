from django.shortcuts import render, HttpResponse

# Create your views here.


def homepage(request):
    return HttpResponse("<h1>First year data here</h1>")

