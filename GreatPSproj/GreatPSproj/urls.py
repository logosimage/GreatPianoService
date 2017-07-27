"""GreatPSproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from accountapp.views import login, register
# from GreatPSproj.templates import.index
from GreatPSapp import views





urlpatterns = [

    url(r'^admin/', admin.site.urls),
    # Accounts
    url(r'^accounts/register/$', register, name='register'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^$',views.index, name='index'),
    url(r'^services/$',views.services, name='services'),
    url(r'^login/$',views.login, name='login'),
    url(r'^schedule_appointment/$',views.schedule_appointment, name='schedule_appointment'),
    url(r'^support/$',views.support, name='support'),
    url(r'^contact/$',views.contact, name='contact')

]
