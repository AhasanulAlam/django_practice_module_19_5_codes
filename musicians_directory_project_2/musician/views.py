from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


# Create your views here.
def userSignup(request):
    if request.method =='POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'User Account Created Successfully!')
            return redirect('signUp_page')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'signup.html', {'form' : register_form, 'type' : 'Register'})


# LOGIN USING CLASS BASED LOGINVIEW:
class UserLoginView(LoginView):
    template_name = 'signup.html'
    def get_success_url(self):
        return reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request, 'User Logged In Successfully!')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, 'Incorrect Logged In Information!')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage') #redirect URL
        return super().dispatch(request, *args, **kwargs)

# LOGOUT USING CLASS BASED LOGOUTVIEW:
class UserLogoutView(LogoutView):
    def get_success_url(self):
        messages.warning(self.request, 'User Logged Out Successfully!')
        return reverse_lazy('homepage')

@login_required
def add_musician(request):
    if request.method =='POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    else:
        musician_form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form' : musician_form})

@login_required
def edit_musician(request, id):
    musician = models.Musician.objects.get(pk=id)
    musician_form = forms.MusicianForm(instance=musician)

    if request.method =='POST': # user sent POST request
        musician_form = forms.MusicianForm(request.POST, instance=musician)  # capture the user post data
        if musician_form.is_valid(): # checking the post data validation
            musician_form.save() # if data valid save in the database
            return redirect('homepage')  # redirect to the page 
    return render(request, 'add_musician.html', {'form' : musician_form})