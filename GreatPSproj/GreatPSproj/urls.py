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
from GreatPSapp import views
from accountapp.views import login, register
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [

                  url(r'^admin/', admin.site.urls),
                  # Accounts
                  url(r'^accounts/register/$', views.scheduling, name='scheduling'),
                  # url(r'^accounts/register/$', register, name='register'),
                  url(r'^accounts/login/$', login, name='login'),
                  url(r'^$', views.template, name='template'),
                  # url(r'^$',views.index, name='index'),
                  url(r'^services/$', views.services, name='services'),
                  url(r'^login/$', views.login, name='login'),
                  url(r'^scheduling/$', views.scheduling, name='scheduling'),
                  url(r'^support/$', views.support, name='support'),
                  url(r'^contact/$', views.contact, name='contact')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
