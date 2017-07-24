from django.shortcuts import render
from django.http import HttpResponse
from.models import Piano
from django.shortcuts import render


def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dic = {'boldmessage': "Jesus is Lord of all!"}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'GreatPSapp/index.html', context=context_dic)

