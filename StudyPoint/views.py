from django.shortcuts import render


def index(request):
    return render(request, 'StudyPoint/index.html', None)


def about(request):
    return render(request, 'StudyPoint/', {})


def contact(request):
    return render(request, 'StudyPoint/', {})



