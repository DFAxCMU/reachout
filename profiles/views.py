from django.shortcuts import render
from reachout import settings

# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse
from .models import Client
#from backend import Client

class ClientProfile(View):
    def get(self, request, client_id):
        print("client id", client_id)
        template = "profile.html"
        client = Client.objects.get(pk = client_id)
        requests = client.request.all()
        context = {
                'client': client,
                'requests': requests,
        }
        return render(request, template, context)

class Timeline(View):
    def get(self, request, client_id):
        print("client id", client_id)
        template = "timeline.html"
        client = Client.objects.get(pk = client_id)
        interactions = client.interaction_client.all().order_by('timestamp')

        context = {
                'client': client,
                'interactions': interactions,
        }
        return render(request, template, context)