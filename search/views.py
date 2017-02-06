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
        full_tags_list   = Tag.objects.all()
        client_list = Client.objects.all()
        template = "search.html"

        search_input = request.POST.get("search_input")
        if (search_input != None): 
            search_input = search_input.lower()

        context = {"client_list": client_list, 
                   "search_input": search_input}
        return render(request, template, context)

    def post(self, request):
        full_client_list = Client.objects.all()
        full_tags_list   = Tag.objects.all()
        client_list      = []
        template         = "search.html"

        search_input = (request.POST.get('search_input'))
        if (search_input != None): search_input = search_input.lower()

        if (search_input == ""): # reset  list
            search_input = "enter tags"
            client_list  = full_client_list

        for client in full_client_list: 
            print("checking client " + client.first_name)
            hasFirst = (client.first_name.lower() == search_input)
            hasLast  = (client.last_name.lower()  == search_input)
            hasNick  = (client.nick_name.lower()  == search_input)

            if (hasFirst or hasLast or hasNick):
                print("  adding client by info")
                client_list.append(client)

            for tag in client.get_tags(): 
                if (tag == search_input and client not in client_list):
                    print("  adding client by tag: " + tag)
                    client_list.append(client)


        context = {"client_list": client_list, 
                   "search_input": search_input}
        return render(request, template, context)