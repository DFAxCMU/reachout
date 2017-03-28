from django.shortcuts import render
from reachout import settings

# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from backend.models import Client
from backend.models import Tag

class Search(View):
    def get(self, request):
        print("Search Page: GET request")
        template = "search.html"
        client_list = Client.objects.all()

        search_input = request.POST.get("search_input")
        if (search_input != None): 
            search_input = search_input.lower()

        context = {"client_list": client_list}
        return render(request, template, context)

    def post(self, request):
        print("Search Page: POST request")
        full_client_list = Client.objects.all()
        client_list      = []
        template         = "search.html"

        search_input = (request.POST.get('search_input'))
        if (search_input != None): search_input = search_input.lower()

        if (search_input == ""): # reset list
            search_input = "enter tags"
            client_list  = full_client_list

        for client in full_client_list: 
            hasFirst = (client.first_name.lower() == search_input)
            hasLast  = (client.last_name.lower()  == search_input)
            hasNick  = (client.nick_name.lower()  == search_input)

            if (hasFirst or hasLast or hasNick):
                client_list.append(client)

            for tag in client.get_tags(): 
                if (client not in client_list and 
                    tag == search_input or 
                    tag in search_input.split() or 
                    search_input in tag.split()):
                    client_list.append(client)


        context = {"client_list": client_list}
        return render(request, template, context)