from django.shortcuts import render
from reachout import settings

# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from backend.models import Client
from backend.models import Tag

from difflib import get_close_matches

class Search(View):
    def get(self, request):
        print("Search Page: GET request")
        template = "search.html"
        client_list = []
        for client in Client.objects.all(): 
            if client.to_show: 
                client_list.append(client)
        tags_list = Tag.objects.all()

        search_input = request.POST.get("search_input")
        if (search_input != None): 
            search_input = search_input.lower()

        try:
            del request.session['editing_status']
        except KeyError:
            pass

        context = {"client_list": client_list}
        return render(request, template, context)

    def post(self, request):
        print("Search Page: POST request")
        full_client_list = Client.objects.all()
        tag_objects_list = Tag.objects.all()

        client_list      = []
        template         = "search.html"


        search_input = (request.POST.get('search_input'))
        if (search_input != None): search_input = search_input.lower()

        if (search_input == ""): # reset list
            search_input = "enter tags"
            client_list  = full_client_list

        for client in full_client_list: 
            client_tags = [client.first_name.lower(), 
                           client.last_name.lower(), 
                           client.nick_name.lower()]

            for tag in client.get_tags(): 
                client_tags.append(tag)

            for tag in client_tags:
                if (client not in client_list and 
                    tag == search_input or 
                    tag in search_input.split() or 
                    search_input in tag.split()):
                    client_list.append(client)

            matches = get_close_matches(search_input, client_tags)

            if (client not in client_list and matches != []):
                client_list.append(client)

        context = {"client_list": client_list}
        return render(request, template, context)