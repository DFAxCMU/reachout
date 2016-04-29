from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django import forms

from backend.models import *

class HomePage(View):
    def get(self, request):
        print("Get HOME")
        context = {}
        if request.user.is_anonymous():
            return render(request, 'start.html', context)
        else:
            return render(request, 'search.html', context)

class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        #TODO: FIX if usernames are not unique, don't crash
        #TODO: fix if user can't log in
        username = request.POST.get('username')
        operation_safety_net = "safety_net"
        if(request.POST.get('organization_code') != "safety_net"):
            return HttpResponseRedirect("/register")
        try:
            User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            new_user = User.objects.create_user(request.POST.get('username'),
                request.POST.get('email'), request.POST.get('password'))
            new_user.first_name = request.POST.get('first_name')
            new_user.last_name = request.POST.get('last_name')
            new_user.save()

            full_name = request.POST.get('first_name') + " " + request.POST.get('last_name')
            cu = CustomUser(name=full_name, user=new_user, email=request.POST.get('email'))
            cu.save()
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/search")
            else:
                #raise forms.ValidationError("Password or username is incorrect")
                return HttpResponseRedirect("/register")
        return HttpResponseRedirect("/register")
        #raise forms.ValidationError(u'This username already exists.')


class Login(View):
    def get(self, request):
        context = {}
        return render(request, 'login.html', context)

    def post(self, request):
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            print("login")
            login(request, user)
            return HttpResponseRedirect("/search")
        else:
            print("can't login")
            #return HttpResponse("Your password is incorrect") 
            #raise forms.ValidationError("Password or username is incorrect")
            return HttpResponseRedirect("/login")

class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")

class UserPage(View):
    def get(self, request):
        context = {}
        return render(request, 'search.html', context)

