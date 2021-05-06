from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated:
        return redirect('resume')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + username)
                return redirect('login')

    context = {'form': form}
    return render(request, 'Register.html', context)


def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('resume')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('resume')
            else:
                messages.info(request,'Username Or password is incorrect')

    context = {}
    return render(request, 'Login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def resume(request):
    context = {}
    return render(request, 'index.html', context)

@login_required(login_url='login')
def create_resume(request):
    context = {}
    return render(request, 'create_resume.html', context)
