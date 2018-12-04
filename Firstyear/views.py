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
    heading = 'GENERAL INFORMATION'
    content_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
    queryset = ''
    subject = 'cp'
    args = {
        'title': title,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset,
        'subject': subject
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def cp_ass(request):
    title = 'C Programming'
    heading = 'ASSIGNMENTS'
    content_text = ''
    queryset = cpAssignment.objects.all()
    subject = 'cp'
    args = {
        'title': title,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset,
        'subject': subject
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def cp_notes(request):
    title = 'C Programming'
    heading = 'NOTES'
    content_text = ''
    queryset = cpNote.objects.all()
    subject = 'cp'
    args = {
        'title': title,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset,
        'subject': subject
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def cp_ebooks(request):
    title = 'C Programming'
    heading = 'EBOOKS'
    content_text = ''
    queryset = cpEbook.objects.all()
    subject = 'cp'
    args = {
        'title': title,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset,
        'subject': subject
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def cp_qpapers(request):
    title = 'C Programming'
    heading = 'Question Papers'
    content_text = ''
    queryset = cpQpaper.objects.all()
    subject = 'cp'
    args = {
        'title': title,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset,
        'subject': subject
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def cp_prac(request):
    title = 'C Programming'
    heading = 'PRACTICALS'
    content_text = 'No Files found!'
    queryset = ''
    subject = 'cp'
    args = {
        'title': title,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset,
        'subject': subject
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


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