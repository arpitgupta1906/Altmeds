from django.shortcuts import render
from .models import UserProfileInfo,headache,malaria
from .forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user and UserProfileInfo.isApproved!=0:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
                # return render(request,'badlogin.html')
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            # return HttpResponse("Invalid login details given")
            return render(request,'badlogin.html')
    else:
        return render(request, 'login.html', {})




def malaria1(request):
    a=malaria.objects.all()
    if request.method=='POST':
        add=request.POST.get('add')
        d=malaria(name=add)
        d.save()
        a=malaria.objects.all()
        return render(request,'malaria.html',{'medicine':a})
    else:
        return render(request,'malaria.html',{'medicine':a})

def headache1(request):
    a=headache.objects.all()
    if request.method=='POST':
        add=request.POST.get('add')
        d=headache(name=add)
        d.save()
        a=headache.objects.all()
        return render(request,'headache.html',{'medicine':a})
    else:
        return render(request,'headache.html',{'medicine':a})
