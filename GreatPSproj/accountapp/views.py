from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import CustomUserCreationForm

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate


def register(request):

    if request.method == "GET":
        form = CustomUserCreationForm(data=request.GET)
    elif request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            user= form.save(commit=False)
            #We can make any last second chages to the user.
            user.save()
            return  redirect('/')

    context = {'form':form}
    return render(request,'register.html', context)



def login(request):
    if request.method == "GET":
        form = AuthenticationForm()

    # 1. handle Post
    elif request.method == "POST":

        # 2. Get form Data
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 3. validate form data
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            # 4. Check Username and password (authenticationForm)
            user = authenticate(username=username, password=password)
            if user:


                # 5. Login (Session)
                django_login(request, user)
                # 6. Redirect
                return redirect('/')

    context = {'form': form}
    return render(request, 'login.html', context)

