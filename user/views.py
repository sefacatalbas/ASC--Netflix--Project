from email import message
from django.shortcuts import render, redirect #varan 32 redirect eklendi
from django.contrib import messages #varan 33 
from django.contrib.auth.models import User #varan 30 
from django.contrib.auth import authenticate, login, logout
from django.urls import is_valid_path #Varan 41
from .forms import * #Varan 61 
# Create your views here.
"""
# Mail İmportu
from django.core.mail import send_mail
from django.conf import settings
"""

def userRegister(request): #varan 23...
    if request.method == 'POST': #varan 29
        username = request.POST['username']
        email = request.POST['email']
        resim = request.FILES['resim']
        tel = request.POST['tel']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2: #varan 31 if/elif/else...s
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Kullanıcı adı kullanımda...')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'Email kullanımda..')
                return redirect('register')
            elif username in password1:
                messages.error(request, 'Kullanıcı adı ile şifre aynı olamaz..')
                return redirect('register')
            elif len(password1) < 6:
                messages.error(request, 'Şifre en az 6 karakter olmalı...')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, email = email, password = password1)
                Account.objects.create(
                    user = user,
                    resim = resim,
                    tel = tel

                )
                user.save()
                messages.success(request, 'Kullanıcı oluşturuldu..')
                return redirect('index')
    return render(request, 'user/register.html') #varan 23 :)

def userLogin(request): #Varan 40
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password=password)

        if user is not None: #42 Varan
            login(request, user)
            messages.success(request, 'Giriş yapıldı...')
            return redirect('profile')
        else:
            messages.error(request, 'Kullanıcı adı hatalı veya şifre hatalı...')
            return redirect('login')
    return render(request, 'user/login.html')

def userLogout(request): #Varan 45 Logout Fonk. oluşturuldu...
    logout(request)
    messages.success(request, 'Çıkış yapıldı...')
    return redirect('index')

def profile(request):  #Varan 51 Browser.html 
    profiles = Profile.objects.filter(user = request.user)
    context = {
        'profiles':profiles
    }
    return render(request, 'browse.html',context)

def createProfile(request): #Varan 62 ---
    form = ProfileForm()
    profile = Profile.objects.filter(user= request.user)
    print(len(profile))
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if len(profile) < 4:
            if form.is_valid():
                profil = form.save(commit= False)
                profil.user = request.user
                print(profil)
                profil.save()
                messages.success(request, 'Profil oluşturuldu...')
                return redirect('profile')
        else:
            messages.error(request, 'Profil sayısı 4den fazla olamaz...')
            return redirect('profile')
    context = {
        'form':form
    }
    return render(request, 'createProfile.html', context)


def hesap(request):
    user = request.user.account
    context = {
        'user':user
    }
    return render(request, 'user/hesap.html')
    

def userDelete(request):
    user = request.user
    user.delete()
    messages.success(request, 'Kullanıcı silindi..')
    return redirect("index")

def update(request):
    user = request.user.account
    form = AccountForm(instance= user)
    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profiliniz güncellendi')
            return redirect("hesap")
    context = {
        'form':form
    }
    return render(request, 'user/update.html', context)