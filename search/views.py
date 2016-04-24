from django.shortcuts import render
from reachout import settings

# Create your views here.
from django.http import HttpResponse
from backend.models import User


def index(request):
    latest_user_list = User.objects.all()
    template = "search.html"
    context = {}

    return render(request, template, context)
