from django.shortcuts import render
from django.http import HttpResponse
from.models import Piano
from django.shortcuts import render



#     # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    #  context_dic = {'boldmessage': "Jesus is Lord of all!"}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    # return render(request, 'GreatPSapp/index.html', context=context_dic)
def template(request):
    return  render(request, 'template.html')

def services(request):
    return render(request, 'services.html')

def login(request):
    return render(request, 'login.html')

def schedule_appointment(request):
    return render(request, 'schedule_appointment.html')

def support(request):
    return render(request, 'support.html')

def contact(request):
    return render(request, 'contact.html')