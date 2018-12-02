from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.


def homepage(request):
    title = 'First Year'
    arg = {
        'title': title
    }
    return render(request, 'Firstyear/home.html', arg)


def physicsstream(request):
    title = 'Physics Sem'
    queryset = phySemSubject.objects.all()
    args = {
        'title': title,
        'subjects': queryset
    }
    return render(request, 'Firstyear/physicssem.html', args)


def chemstream(request):
    title = 'Chemistry Sem'
    queryset = chemSemSubject.objects.all()
    args = {
        'title': title,
        'subjects': queryset
    }
    return render(request, 'Firstyear/chemsem.html', args)


def chemistry(request):
    title = 'Chemistry'
    args = {
        'title': title
    }
    return render(request, 'Firstyear/chemistry.html')


def physics(request):
    title = 'Physics'
    args = {
        'title': title
    }
    return render(request, 'Firstyear/physics.html')


def ee(request):
    title = 'Electrical Engineering'
    args = {
        'title': title
    }
    return render(request, 'Firstyear/ee.html')


def em(request):
    title = 'Engineering Mechanics'
    args = {
        'title': title
    }
    return render(request, 'Firstyear/em.html')


def cp(request):
    title = 'C Programming'
    args = {
        'title': title
    }
    return render(request, 'Firstyear/cp.html')


def ed(request):
    title = 'Engineering Drawing'
    args = {
        'title': title
    }
    return render(request, 'Firstyear/ed.html')


def maths(request):
    title = 'Maths'
    args = {
        'title': title
    }
    return render(request, 'Firstyear/maths.html')


def ss(request):
    title = 'Social Science'
    args = {
        'title': title
    }
    return render(request, 'Firstyear/ss.html')


def cs(request):
    title = 'Communication Skill'
    args = {
        'title': title
    }
    return render(request, 'Firstyear/cs.html')