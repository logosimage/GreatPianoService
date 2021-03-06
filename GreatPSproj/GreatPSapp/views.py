from django.shortcuts import render, HttpResponse

from .models import Service_Request
from .models import Scheduling
from accountapp.models import User


#     # Construct a dictionary to pass to the template engine as its context.
# Note the key boldmessage is the same as {{ boldmessage }} in the template!
#  context_dic = {'boldmessage': "Jesus is Lord of all!"}
# Return a rendered response to send to the client.
# We make use of the shortcut function to make our lives easier.
# Note that the first parameter is the template we wish to use.
# return render(request, 'GreatPSapp/index.html', context=context_dic)
def template(request):
    return render(request, 'template.html')


def services(request):
    return render(request, 'services.html')


def login(request):
    return render(request, 'login.html')

# def schedulings(request):
#     if request.method == 'POST':
#         print(request.POST)    

def User(request):
    if request.method == 'POST':
        print(request.POST)

        form = User()
        cell_phone = request.POST.get('cell_phone', None)

        work_phone = request.POST.get('work_phone', None)
        
        home_phone = request.POST.get('home_phone', None)
        
        address = request.POST.get('address', None)
        
        city = request.POST.get('city', None)
        
        state = request.POST.get('state', None)
        
        zip = request.POST.get('zip', None)

        form.save()

def scheduling(request):
    if request.method == 'POST':
        print(request.POST)
        form = Service_Request()

        form.requested_date = ' '.join(request.POST.getlist('apt_day', ['none entered']))

        form.requested_time = ' '.join(request.POST.getlist('apt_time', ['none entered']))

        type_of_service = request.POST.getlist('service_type', None)

        if 'tuning' in type_of_service:
            form.tune = 'tuning'
        else:
            form.tune = ''

        if 'regulation' in type_of_service:
            form.regulation = 'regulation'
        else:
            form.regulation = ''

        if 'repair' in type_of_service:
            form.repair = 'repair'
        else:
            form.repair = ''

        if 'keys' in type_of_service:
            form.key_services = 'keys'
        else:
            form.key_services = ''

        if 'contract' in type_of_service:
            form.annual_contract = 'contract'
        else:
            form.annual_contract = ''

        if 'cleaning' in type_of_service:
            form.cleaning = 'cleaning'
        else:
            form.cleaning = ''

        if 'appraisal' in type_of_service:
            form.appraisal = 'appraisal'
        else:
            form.appraisal = ''

        if 'consult' in type_of_service:
            form.purchase_consulting = 'consult'
        else:
            form.purchase_consulting = ''

        form.pref_date_time = request.POST.get('pref-date-time', '')

        form.save()

        return HttpResponse('<h1> Thank you for submission. We will be contacting you within the next day.</h1><p><a id="item1" href="/">Home</a>')

    return render(request, 'scheduling.html')


def support(request):
    return render(request, 'support.html')


def contact(request):
    return render(request, 'contact.html')
