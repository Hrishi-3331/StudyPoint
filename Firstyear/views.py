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


# Chemistry
def chem(request):
    title = 'Chemistry'
    subject = 'chem'
    heading = 'GENERAL INFORMATION'
    content_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
    queryset = ''
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def chem_ass(request):
    title = 'Chemistry'
    subject = 'chem'
    heading = 'ASSIGNMENTS'
    content_text = ''
    queryset = chemAssignment.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def chem_notes(request):
    title = 'Chemistry'
    subject = 'chem'
    heading = 'NOTES'
    content_text = ''
    queryset = chemNote.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def chem_ebooks(request):
    title = 'Chemistry'
    subject = 'chem'
    heading = 'EBOOKS'
    content_text = ''
    queryset = chemEbook.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def chem_qpapers(request):
    title = 'Chemistry'
    subject = 'chem'
    heading = 'QUESTION PAPERS'
    content_text = ''
    queryset = chemQpaper.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def chem_prac(request):
    title = 'Chemistry'
    subject = 'chem'
    heading = 'PRACTICALS'
    content_text = ''
    queryset = chemPractical.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


# Physics
def physics(request):
    title = 'Physics'
    subject = 'physics'
    heading = 'GENERAL INFORMATION'
    content_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
    queryset = ''
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def physics_ass(request):
    title = 'Physics'
    subject = 'physics'
    heading = 'ASSIGNMENTS'
    content_text = ''
    queryset = physicsAssignment.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def physics_notes(request):
    title = 'Physics'
    subject = 'physics'
    heading = 'NOTES'
    content_text = ''
    queryset = physicsNote.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def physics_ebooks(request):
    title = 'Physics'
    subject = 'physics'
    heading = 'EBOOKS'
    content_text = ''
    queryset = physicsEbook.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def physics_qpapers(request):
    title = 'Physics'
    subject = 'physics'
    heading = 'QUESTION PAPERS'
    content_text = ''
    queryset = physicsQpaper.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def physics_prac(request):
    title = 'Physics'
    subject = 'physics'
    heading = 'PRACTICALS'
    content_text = ''
    queryset = physicsPractical.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


# Electrical Engineering
def ee(request):
    title = 'Electrical Engineering'
    heading = 'GENERAL INFORMATION'
    content_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
    queryset = ''
    subject = 'ee'
    args = {
        'title': title,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset,
        'subject': subject
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def ee_ass(request):
    title = 'Electrical Engineering'
    heading = 'ASSIGNMENTS'
    content_text = ''
    queryset = eeAssignment.objects.all()
    subject = 'ee'
    args = {
        'title': title,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset,
        'subject': subject
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def ee_notes(request):
    title = 'Electrical Engineering'
    heading = 'NOTES'
    content_text = ''
    queryset = eeNote.objects.all()
    subject = 'ee'
    args = {
        'title': title,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset,
        'subject': subject
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def ee_ebooks(request):
    title = 'Electrical Engineering'
    heading = 'EBOOKS'
    content_text = ''
    queryset = eeEbook.objects.all()
    subject = 'ee'
    args = {
        'title': title,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset,
        'subject': subject
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def ee_qpapers(request):
    title = 'Electrical Engineering'
    heading = 'Question Papers'
    content_text = ''
    queryset = eeQpaper.objects.all()
    subject = 'ee'
    args = {
        'title': title,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset,
        'subject': subject
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def ee_prac(request):
    title = 'Electrical Engineering'
    heading = 'PRACTICALS'
    content_text = 'No Files found!'
    queryset = eePractical.objects.all()
    subject = 'ee'
    args = {
        'title': title,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset,
        'subject': subject
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


# Engineeering Mechanics
def em(request):
    title = 'Engineering Mechanics'
    subject = 'em'
    heading = 'GENERAL INFORMATION'
    content_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
    queryset = ''
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def em_ass(request):
    title = 'Engineering Mechanics'
    subject = 'em'
    heading = 'ASSIGNMENTS'
    content_text = ''
    queryset = emAssignment.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def em_notes(request):
    title = 'Engineering Mechanics'
    subject = 'em'
    heading = 'NOTES'
    content_text = ''
    queryset = emNote.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def em_ebooks(request):
    title = 'Engineering Mechanics'
    subject = 'em'
    heading = 'EBOOKS'
    content_text = ''
    queryset = emEbook.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def em_qpapers(request):
    title = 'Engineering Mechanics'
    subject = 'em'
    heading = 'QUESTION PAPERS'
    content_text = ''
    queryset = emQpaper.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def em_prac(request):
    title = 'Engineering Mechanics'
    subject = 'em'
    heading = 'PRACTICALS'
    content_text = ''
    queryset = emPractical.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


# Computer Programming
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
    heading = 'QUESTION PAPERS'
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
    content_text = ''
    queryset = cpPractical.objects.all()
    subject = 'cp'
    args = {
        'title': title,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset,
        'subject': subject
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


# Engineering Drawing
def ed(request):
    title = 'Engineering Drawing'
    subject = 'ed'
    heading = 'GENERAL INFORMATION'
    content_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
    queryset = ''
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def ed_ass(request):
    title = 'Engineering Drawing'
    subject = 'ed'
    heading = 'ASSIGNMENTS'
    content_text = ''
    queryset = edAssignment.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def ed_notes(request):
    title = 'Engineering Drawing'
    subject = 'ed'
    heading = 'NOTES'
    content_text = ''
    queryset = edNote.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def ed_ebooks(request):
    title = 'Engineering Drawing'
    subject = 'ed'
    heading = 'EBOOKS'
    content_text = ''
    queryset = edEbook.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def ed_qpapers(request):
    title = 'Engineering Drawing'
    subject = 'ed'
    heading = 'QUESTION PAPERS'
    content_text = ''
    queryset = edQpaper.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def ed_prac(request):
    title = 'Engineering Drawing'
    subject = 'ed'
    heading = 'PRACTICALS'
    content_text = ''
    queryset = edPractical.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


# Mathematics
def maths(request):
    title = 'Maths'
    subject = 'maths'
    heading = 'GENERAL INFORMATION'
    content_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
    queryset = ''
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def maths_ass(request):
    title = 'Maths'
    subject = 'maths'
    heading = 'ASSIGNMENTS'
    content_text = ''
    queryset = mathsAssignment.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def maths_notes(request):
    title = 'Maths'
    subject = 'maths'
    heading = 'NOTES'
    content_text = ''
    queryset = mathsNote.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def maths_ebooks(request):
    title = 'Maths'
    subject = 'maths'
    heading = 'EBOOKS'
    content_text = ''
    queryset = mathsEbook.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def maths_qpapers(request):
    title = 'Maths'
    subject = 'maths'
    heading = 'QUESTION PAPERS'
    content_text = ''
    queryset = mathsQpaper.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def maths_prac(request):
    title = 'Maths'
    subject = 'maths'
    heading = 'PRACTICALS'
    content_text = ''
    queryset = mathsPractical.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


# Social Science
def ss(request):
    title = 'Social Science'
    subject = 'ss'
    heading = 'GENERAL INFORMATION'
    content_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
    queryset = ''
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def ss_ass(request):
    title = 'Social Science'
    subject = 'ss'
    heading = 'ASSIGNMENTS'
    content_text = ''
    queryset = ssAssignment.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def ss_notes(request):
    title = 'Social Science'
    subject = 'ss'
    heading = 'NOTES'
    content_text = ''
    queryset = ssNote.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def ss_ebooks(request):
    title = 'Social Science'
    subject = 'ss'
    heading = 'EBOOKS'
    content_text = ''
    queryset = ssEbook.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def ss_qpapers(request):
    title = 'Social Science'
    subject = 'ss'
    heading = 'QUESTION PAPERS'
    content_text = ''
    queryset = ssQpaper.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def ss_prac(request):
    title = 'Social Science'
    subject = 'ss'
    heading = 'PRACTICALS'
    content_text = ''
    queryset = ssPractical.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


# Communication Skills
def cs(request):
    title = 'Communication Skills'
    subject = 'cs'
    heading = 'GENERAL INFORMATION'
    content_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
    queryset = ''
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def cs_ass(request):
    title = 'Communication Skills'
    subject = 'cs'
    heading = 'ASSIGNMENTS'
    content_text = ''
    queryset = csAssignment.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def cs_notes(request):
    title = 'Communication Skills'
    subject = 'cs'
    heading = 'NOTES'
    content_text = ''
    queryset = csNote.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def cs_ebooks(request):
    title = 'Communication Skills'
    subject = 'cs'
    heading = 'EBOOKS'
    content_text = ''
    queryset = csEbook.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def cs_qpapers(request):
    title = 'Communication Skills'
    subject = 'cs'
    heading = 'QUESTION PAPERS'
    content_text = ''
    queryset = csQpaper.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)


def cs_prac(request):
    title = 'Communication Skills'
    subject = 'cs'
    heading = 'PRACTICALS'
    content_text = ''
    queryset = csPractical.objects.all()
    args = {
        'title': title,
        'subject': subject,
        'heading': heading,
        'content_text': content_text,
        'queryset': queryset
    }
    return render(request, 'Firstyear/firstyearbase.html', args)