from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse
from backend.models import *

#from .models import Tag
class UpdateQuickInfo(View):
    print("here")
    def get(self, request, client_id):
        print("UpdateInfo GET REquest")
        template = "quickinfo.html"
        # request["cid"] = client_id
        context = {}
        context["cid"] = client_id
        print(request)
        return render(request, template, context)
    def post(self, request, client_id):
        print("updateInfo POST request")
        client = Client.objects.get(pk = client_id)
        # client.last_name
        client.is_military     = True if request.POST.get("is_military") == "yes" else False
        client.health_concerns = True if request.POST.get("health_concerns") == "yes" else False
        client.dna_assistance  = True if request.POST.get("dna_assistance") == "yes" else False
        client.has_doctor      = True if request.POST.get("has_doctor") == "yes" else False
        client.has_insurance   = True if request.POST.get("has_insurance") == "yes" else False
        client.duration_of_homelessness = request.POST.get("duration")
        print(client.is_military)
        client.save()
        return HttpResponseRedirect("/client/" + str(client_id))

# def LoggingInfoOne(request, client_id):
#     context = {}
#     context["cid"] = client_id
#     return render(request, 'logging-info-1.html', context)

# def LoggingInfoTwo(request, client_id):
#     context = {}
#     context["cid"] = client_id
#     return render(request, 'logging-info-2.html', context)

# def LoggingInfoThree(request, client_id):
#     context = {}
#     context["cid"] = client_id
#     return render(request, 'logging-info-3.html', context)

# def TitleAndDescription(request, client_id):
#     title =  request.POST.get("title")
#     description =  request.POST.get("description")

#     print("title " + title)
#     print("description " + description)
#     client = Client.objects.get(pk = client_id)
#     i = Interaction(description=description, title=title, client = client, user = request.user.customuser)
#     i.save()
#     context = {}
#     context["cid"] = client_id
#     return JsonResponse({"worked": True})

# def ShortQuestions(request, client_id):
#     q1 =  request.POST.get("q1")
#     q2 =  request.POST.get("q2")
#     q3 =  request.POST.get("q3")
#     q4 =  request.POST.get("q4")
#     q5 =  request.POST.get("q5")
#     client = Client.objects.get(pk = client_id)
#     client.is_military = True if q1 == "yes" else False
#     client.health_concerns = True if q2 == "yes" else False
#     client.dna_assistance = True if q3 == "yes" else False
#     client.has_doctor = True if q4 == "yes" else False
#     client.duration_of_homelessness = True if q5 == "yes" else False
#     client.save()

#     context = {}
#     context["cid"] = client_id
#     context["requests"] = client.request.all()
#     return render(request, 'logging-info-3.html', context)

# def LogAllInfo(request, client_id):
#     item_name =  request.POST.get("item_name")
#     item_amount =  request.POST.get("amount")
#     print("--------------------")
#     print(item_name)
#     print(item_amount)
#     i = Item(name = item_name, amount = item_amount)
#     i.save()  
#     client = Client.objects.get(pk = client_id)
#     request = Requests(item = i, client_profile = client)
#     request.save()
#     return JsonResponse({"worked": True})   