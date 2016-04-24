from django.shortcuts import render
from django.http import HttpResponse


def LoggingInfoOne(request):
    print("Inside of LoggingInfoOne")
    return render(request, 'logging-info-1.html')

def TitleAndDescription(request, client_id):
    print("Inside of TitleAndDescription")
    title =  request.POST.get("title")
    description =  request.POST.get("description")
    client = Client.objects.get(pk = client_id)
    # context = {}
    # context["title"] = title
    # context["description"] = description
    # #print("title:"+title)
    # #print("description:"+description)
    i = Interaction(description=description, title=title, client = client)
    i.save()
    return render(request, 'logging-info-2.html')

def ShortQuestions(request):
    title =  request.POST.get("ititle")
    descrip =  request.POST.get("idescription")
    q1 =  request.POST.get("q1")
    q2 =  request.POST.get("q2")
    q3 =  request.POST.get("q3")
    q4 =  request.POST.get("q4")
    q5 =  request.POST.get("q5")
    context = {}
    context["title"] = title
    context["description"] = descrip
    context["q1"] = q1
    context["q2"] = q2
    context["q3"] = q3
    context["q4"] = q4
    context["q5"] = q5
    return render(request, 'logging-info-3.html', context)

def LogAllInfo(request):
    title =  request.POST.get("ititle")
    descrip =  request.POST.get("idescription")
    q1 =  request.POST.get("q1")
    q2 =  request.POST.get("q2")
    q3 =  request.POST.get("q3")
    q4 =  request.POST.get("q4")
    q5 =  request.POST.get("q5")
    q6 = request.POST.get("q6")
    c=Client(is_military = q1, duration_of_homelessness = q6,
    health_concerns = q2, dna_assistance = q3, has_doctor = q4, 
                            has_insurance = q5)
    c.save()
    i = Interaction(client=c, description=descrip)
    i.save()
    return render(request, 'NEXT')    