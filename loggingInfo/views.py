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
