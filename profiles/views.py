from django.shortcuts import render
from reachout import settings

# Create your views here.
from django.http import HttpResponse


def index(request):
    template = "profile.html"
    context = {}

    return render(request, template, context)