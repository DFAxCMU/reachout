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
        first_name = request.POST.get("first_name")
        nick_name = request.POST.get("nick_name")
        if (first_name == "" and nick_name == ""):
            #blocked by frontend 
            return HttpResponseRedirect("/new_client")
        client = Client.objects.filter(first_name=first_name,nick_name=nick_name)
        if (len(client) > 0):
            # return HttpResponse("User already exists!")
            return render(request, 'new_client.html', {
                'error_message': "Client already exists",
            })
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
        template = "profile.html"
        current_client = Client.objects.get(pk = client_id)
        requests = current_client.request.all().order_by('asked_timestamp')
        interactions = Interaction.objects.filter(client=current_client).order_by('-timestamp')
        
        status = 'none'
        if (request.session.get('editing_status')): 
            status = request.session.get('editing_status')
        
        try:
            del request.session['editing_status']
        except KeyError:
            pass

        context = {
                'client': current_client,
                'requests': requests,
                'interactions': interactions,
                'status' : status
        }
        return render(request, template, context)
    def post(self, request, client_id): 
        for key, value in request.POST.items():
            print(key, value)
        if (request.POST.get("duration", default="NO") != "NO"):
            return updateQuickInfo(self, request, client_id)
        if (request.POST.get("newrequestvalue", default="NO") != "NO"):
            return updateRequests(self, request, client_id)
        if (request.POST.get("updatefirstname", default="NO") != "NO"):
            return updateName(self, request, client_id)
        if (request.POST.get("newtagvalue", default="NO") != "NO"):
            return updateTags(self, request, client_id)

        if (request.POST.get("deletetagdesc", default="NO") != "NO"): 
            print('deleting tag')
            return deleteTag(self, request, client_id)

        if (request.POST.get("deletereqdesc", default="NO") != "NO"): 
            print("deleting request")
            return deleteRequest(self, request, client_id);

class DeleteClient(View):
    def get(self, request, client_id):
        template = "delete_client.html"
        context = {
            "cid": client_id
        }
        return render(request, template, context)
    def post(self, request, client_id):
        client = Client.objects.get(pk=client_id)
        client.to_show = False
        client.save()
        return HttpResponseRedirect("/search")
 

def updateRequests(self, request, client_id):
    if (request.POST.get("newrequestvalue") != ""):
        client = Client.objects.get(pk = client_id)
        new_request = Requests(description = request.POST.get("newrequestvalue"), 
                              client_profile = client)
        new_request.save()
    request.session['editing_status'] = "created new request"
    return HttpResponseRedirect("/client/" + str(client_id))


def updateName(self, request, client_id):
    client = Client.objects.get(pk = client_id)
    client.first_name = request.POST.get("updatefirstname")
    client.nick_name = request.POST.get("updatenickname")
    client.last_name = request.POST.get("updatelastname")
    client.save()
    request.session['editing_status'] = "updated client name"
    return HttpResponseRedirect("/client/" + str(client_id))

def deleteRequest(self, request, client_id): 
    client = Client.objects.get(pk = client_id)
    Requests.objects.filter(id=request.POST.get("deletereqdesc")).delete()
    request.session['editing_status'] = "deleted request"
    return HttpResponseRedirect("/client/" + str(client_id))

def deleteTag(self, request, client_id): 
    client = Client.objects.get(pk = client_id)
    for tag in Tag.objects.all(): 
        if (client in tag.client.all()):
            if (tag.name.lower() == request.POST.get("deletetagdesc")): 
                tag.delete()
    request.session['editing_status'] = "deleted tag"
    return HttpResponseRedirect("/client/" + str(client_id))

def enterTag(self, request, client_id): 
    client = Client.objects.get(pk = client_id)
    for tag in Tag.objects.all(): 
        if (client in tag.client.all()):
            if (tag.name.lower() == request.POST.get("entertagsubmit")): 
                tag.add()
    request.session['editing_status'] = "created new tag"
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
    request.session['editing_status'] = "updated quick info"
    return HttpResponseRedirect("/client/" + str(client_id))

def updateTags(self, request, client_id):
    if request.POST.get("newtagvalue") != "":
        client = Client.objects.get(pk = client_id)
        new_tag = Tag(name = request.POST.get("newtagvalue"))
        new_tag.save()
        new_tag.client.add(client)
        new_tag.save()
        request.session['editing_status'] = "created new tag"
    else:
        request.session['editing_status'] = "can't add an empty tag"
    return HttpResponseRedirect("/client/" + str(client_id))

class Timeline(View):
    def get(self, request, client_id):
        template = "timeline.html"
        client = Client.objects.get(pk = client_id)
        interactions = client.interaction_client.all().order_by('timestamp')

        context = {
                'client': client,
                'interactions': interactions,
        }
        return render(request, template, context)

class EditRequest(View):
    def get(self, request, client_id, request_id):
        template = "edit_request.html"
        req = Requests.objects.get(pk=request_id)
        context = {"cid": client_id,"request_description" : req.description}
        return render(request, template, context)
    def post(self, request, client_id, request_id):
        client = Client.objects.get(pk=client_id)
        user = CustomUser.objects.all()[0]
        new_description = request.POST.get("description")
        if (new_description == ""):
            request.session['editing_status'] = "can't add an empty request"
            return HttpResponseRedirect("/client/" + str(client_id))
        req = Requests.objects.get(pk=request_id)
        req.description = new_description
        req.save()
        request.session['editing_status'] = "edited request"
        return HttpResponseRedirect("/client/" + str(client_id))


class EditStory(View):
    def get(self, request, client_id):
        template = "edit_story.html"
        client = Client.objects.get(pk=client_id)
        context = {"cid": client_id,"story" : client.story}
        return render(request, template, context)

    def post(self, request, client_id):
        client = Client.objects.get(pk=client_id)
        #user = CustomUser.objects.all()[0]
        new_story = request.POST.get("story")
        if (new_story == ""):
            request.session['editing_status'] = "can't add an empty story"
            return HttpResponseRedirect("/client/" + str(client_id))
        client = Client.objects.get(pk=client_id)
        client.story = new_story
        client.save()
        request.session['editing_status'] = "edited story"
        return HttpResponseRedirect("/client/" + str(client_id))



class EditName(View):
    def get(self, request, client_id):
        template = "edit_name.html"
        client = Client.objects.get(pk = client_id)
        context = {"cid": client_id, "client": client}
        return render(request, template, context)
    def post(self, request, client_id):
        client = Client.objects.get(pk=client_id)
        new_first_name = request.POST.get("first_name")
        new_nick_name = request.POST.get("nick_name")
        new_last_name = request.POST.get("last_name")
        print("firstname: " + new_first_name)
        print("nickname: " + new_nick_name)
        print("lastname: " + new_last_name)
        if (new_first_name == "" or new_last_name == ""):
            #this should not be possible b/c of the front end
            request.session['editing_status'] = "please add a first and last name"
            return HttpResponseRedirect("/client/" + str(client_id))
        client = Client.objects.get(pk=client_id)
        client.first_name = new_first_name
        client.nick_name = new_nick_name
        client.last_name = new_last_name
        client.save()
        request.session['editing_status'] = "edited name"        
        return HttpResponseRedirect("/client/" + str(client_id))









