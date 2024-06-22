from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms
from django.views.generic import View

# Create your views here.

def logout_user(request):
    logout(request)
    return redirect('login')

class LoginPage(View):
    class_form = form = forms.LoginForm
    template_name = 'authentication/login.html'

    def get(self, request):
        form = self.class_form()
        message = ""
        return render(request, self.template_name , context={'form': form, 'message': message})


    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
 
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Identifiants invalides.'

        return render(request, self.template_name , context={'form': form, 'message': message})


def login_page(request):
    form = forms.LoginForm()
    message = ""
    
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
 
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Identifiants invalides.'

    return render(request, 'authentication/login.html', context={'form': form, 'message': message})






