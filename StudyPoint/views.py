from django.shortcuts import render


def index(request):
    return render(request, 'StudyPoint/index.html', None)


def about(request):
    return render(request, 'StudyPoint/about.html', None)


def contactus(request):
    return render(request, 'StudyPoint/contact.html', None)






