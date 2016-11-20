from django.shortcuts import render
from reachout import settings

# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse
from .models import *
  
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
        current_client = Client.objects.get(pk = client_id)
        requests = current_client.request.all()
        interactions = Interaction.objects.filter(client=current_client)
        context = {
                'client': current_client,
                'requests': requests,
                'interactions': interactions,
        }
        return render(request, template, context)
    def post(self, request, client_id): 
        print("in views post")
        for key, value in request.POST.items():
            print(key, value)
        if (request.POST.get("duration", default="NO") != "NO"):
            print("updateinfo update")
            return updateQuickInfo(self, request, client_id)
        if (request.POST.get("newrequestvalue", default="NO") != "NO"):
            print("newrequestvalue update")
            return updateRequests(self, request, client_id)
        if (request.POST.get("updatefirstname", default="NO") != "NO"):
            print("\\nn\n\n\n\nn\n\n\n\n\n\n\n\n\n\n")
            return updateName(self, request, client_id)

        if (request.POST.get("newtagvalue", default="NO") != "NO"):
            print("\n\n\nupdateTags update\n\n\n")
            return updateTags(self, request, client_id)

        if (request.POST.get("requestID", default="NO") != "NO"): 
            print("\n\n\ndeleting request\n\n\n")
            return deleteRequest(self, request, client_id);

        if (request.POST.get("deletetagdesc", default="NO") != "NO"): 
            print("\n\nupdateTags update\n\n")
            return deleteTag(self, request, client_id)
        print("none found")

def updateRequests(self, request, client_id):
    print("updateInfo POST request")
    if (request.POST.get("newrequestvalue") != ""):
        client = Client.objects.get(pk = client_id)
        # print("newrequestvalue: " + newrequestvalue)
        new_request = Requests(description = request.POST.get("newrequestvalue"), 
                              client_profile = client)
        new_request.save()

    return HttpResponseRedirect("/client/" + str(client_id))

def updateName(self, request, client_id):
    print("UPDATING NAME POST request")
    client = Client.objects.get(pk = client_id)
    client.first_name = request.POST.get("updatefirstname")
    client.nick_name = request.POST.get("updatenickname")
    client.last_name = request.POST.get("updatelastname")
    client.save()
    return HttpResponseRedirect("/client/" + str(client_id))

def deleteRequest(self, request, client_id): 
    print("deleteRequest POST request")
    client = Client.objects.get(pk = client_id)
    print("--------------")
    print(request.POST.get("requestID"));
    print("-------")
    Requests.objects.filter(id=request.POST.get("requestID")).delete()
    print("--deleted-----")

    return HttpResponseRedirect("/client/" + str(client_id))

def deleteTag(self, request, client_id): 
    print("deleteRequest POST request")
    client = Client.objects.get(pk = client_id)
    print("--------------")
    print(request.POST.get("deletetagdesc"));
    print (client.get_tags())
    print("-------")
    for tag in Tag.objects.all(): 
        if (client in tag.client.all()):
            if (tag.name.lower() == request.POST.get("deletetagdesc")): 
                print("going to delete", tag.name)
                tag.delete()

    # Tag.objects.filter(name=request.POST.get("deletetagdesc")).delete()
    print("--deleted-----")

    return HttpResponseRedirect("/client/" + str(client_id))

def updateQuickInfo(self, request, client_id): 
    print("updateInfo POST request")
    client = Client.objects.get(pk = client_id)
    client.is_military     = (request.POST.get("is_military") == "yes")
    client.health_concerns = (request.POST.get("health_concerns") == "yes")
    client.dna_assistance  = (request.POST.get("dna_assistance") == "yes")
    client.has_doctor      = (request.POST.get("has_doctor") == "yes")
    client.has_insurance   = (request.POST.get("has_insurance") == "yes")
    client.duration_of_homelessness = request.POST.get("duration")
    client.save()
    return HttpResponseRedirect("/client/" + str(client_id))

def updateTags(self, request, client_id):
    print("updateTags POST request")
    client = Client.objects.get(pk = client_id)
    # print("newrequestvalue: " + newrequestvalue)
    new_tag = Tag(name = request.POST.get("newtagvalue"))
    new_tag.save()
    new_tag.client.add(client)
    new_tag.save()
    return HttpResponseRedirect("/client/" + str(client_id))

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


