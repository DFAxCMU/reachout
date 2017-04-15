from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django import forms

from backend.models import *

class HomePage(View):
    def get(self, request):
        context = {}
        if request.user.is_anonymous():
            return render(request, 'start.html', context)
        else:
            return HttpResponseRedirect("/search")

class Register(View):
    def get(self, request):
        reg_attempt = {
            "first_name": "",
            "last_name":  "",  
            "email":  "",
            "user":  "", 
            "org_code": "" 
        }
        return render(request, 'register.html',reg_attempt)

    def post(self, request):
        saved_fields = {
            "first_name": request.POST.get("first_name"),
            "last_name":  request.POST.get("last_name"),
            "email":  request.POST.get("email"),
            "username":  request.POST.get("username"), 
            "org_code": request.POST.get("organization_code")
        }
        username = request.POST.get('username')
        operation_safety_net = "safety_net"
        if(request.POST.get('organization_code') != "safety_net"):
            saved_fields["error_message"] = "Organization code is incorrect"
            return render(request, 'register.html',saved_fields)
        if(request.POST.get('password') != request.POST.get('repassword')):
            saved_fields["error_message"] = "Passwords do not match"
            return render(request, 'register.html', saved_fields)        
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
                saved_fields["error_message"] = "Password or username is incorrect"
                return render(request, 'register.html',saved_fields)
        saved_fields["error_message"] = "This username already exists"
        return render(request, 'register.html',saved_fields)

class Login(View):
    def get(self, request):
        context = {}
        return render(request, 'login.html', context)

    def post(self, request):
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/search")
        else:
            return render(request, 'login.html', {
                'error_message': "Your password or username is incorrect",
            })

class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")

class UserPage(View):
    def get(self, request):
        context = {}
        return render(request, 'search.html', context)

