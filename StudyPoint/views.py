from django.shortcuts import render


def index(request):
    return render(request, 'StudyPoint/index.html', None)


def about(request):
    title = 'About Us'
    args = {
        'title': title,
            }
    return render(request, 'StudyPoint/about.html', args)


def contactus(request):
    title = 'Contact Us'
    args = {'title': title}
    return render(request, 'StudyPoint/contact.html', args)






