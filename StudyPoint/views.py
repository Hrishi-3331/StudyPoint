from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from django.views.generic import View


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


class SignupFormView(View):
    form_class = SignupForm

    def get(self, request):
        form = self.form_class(None)
        title = 'SignUp | StudyPoint'
        return render(request, 'StudyPoint/signup.html', {'form': form, 'title':title})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            idnumber = form.cleaned_data.get('idnumber')
            email = form.cleaned_data.get('email')

            user.save()

            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('homepage')


class LoginFormView(View):
    form_class = LoginForm

    def get(self, request):
        form = self.form_class(None)
        title = 'Login| VNIT StudyPoint'
        args = {
            'title': title,
            'form': form
        }
        return render(request, 'StudyPoint/login.html', args)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage')

            else:
                return redirect('login')


def logOut(request):
    logout(request)
    return redirect('login')










