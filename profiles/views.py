from django.shortcuts import render
from reachout import settings

# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse
from .models import Client
from .models import Tag
#from backend import Client

class NewClientProfile(View):
    def get(self, request):
        template = "new_client.html"
        return render(request, template)
    def post(self,request):
        new_client = Client(first_name = request.POST.get("first_name"),
            last_name = request.POST.get("last_name"),
            nick_name = request.POST.get("nick_name"), 
            story     = request.POST.get("story"))
        new_client.save()
        new_client_id = new_client.id
        for tag in (request.POST.get("tags")).split(","): 
            tag = tag.strip()
            if (tag != ""):
                new_tag = Tag(name=tag.strip())
                new_tag.save()
                new_tag.client.add(new_client)
        return HttpResponseRedirect("/client/" + str(new_client_id))

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