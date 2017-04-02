from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse
from backend.models import *

class LogInteraction(View):
    def get(self, request, client_id):
        template = "log_interaction.html"
        context = {"cid": client_id}
        return render(request, template, context)
    def post(self, request, client_id):
        print("post logINteraction")
        client = Client.objects.get(pk=client_id)
        print(request.user)
        print(type(request.user))
        # user = CustomUser.objects.filter(name=request.user)
        print(CustomUser.objects.all()[0])
        user = CustomUser.objects.all()[0]
        description = request.POST.get("description")
        title = "" #take this out of the model?
        new_interaction = Interaction(description=description, 
                                      title=title, 
                                      client=client, 
                                      user=user)
        new_interaction.save()
        return HttpResponseRedirect("/client/" + str(client_id))

class EditInteraction(View):
    def get(self, request, client_id,interaction_id):
        template = "edit_interaction.html"
        interaction = Interaction.objects.get(pk=interaction_id)
        context = {"cid": client_id,"interaction_description" : interaction.description}
        return render(request, template, context)
    def post(self, request, client_id,interaction_id):
        client = Client.objects.get(pk=client_id)
        user = CustomUser.objects.all()[0]
        new_description = request.POST.get("description")
        interaction = Interaction.objects.get(pk=interaction_id)
        interaction.description = new_description
        interaction.save()
        return HttpResponseRedirect("/client/" + str(client_id))

class DeleteInteraction(View):
    def get(self, request, client_id,interaction_id):
        template = "delete_interaction.html"
        interaction = Interaction.objects.get(pk=interaction_id)
        context = {
            "cid": client_id,
            "interaction_description" : interaction.description,
            "interaction_timestamp": interaction.timestamp,
            "interaction_user": interaction.user, 
        }
        return render(request, template, context)
    def post(self, request, client_id,interaction_id):
        client = Client.objects.get(pk=client_id)
        user = CustomUser.objects.all()[0]
        interaction = Interaction.objects.get(pk=interaction_id)
        interaction.delete()
        return HttpResponseRedirect("/client/" + str(client_id))
