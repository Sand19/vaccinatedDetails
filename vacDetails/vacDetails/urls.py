"""vacDetails URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Staff Vaccines Details Administrator"
admin.site.site_title = "Staff Vaccines Details"
admin.site.site_url = "/vacDetails"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacDetails/', include("staff.urls")),
]

'''
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from django.urls import path
#from . import views
import users
#from filebrowser.sites import site

admin.site.site_header = "Technology Innovation Group Administrator"
admin.site.site_title = "Technology Innovation Group"
admin.site.site_url = "/projects" #"http://localhost:8000/admin/"
#app_name = 'main'  # here for namespacing of urls.
#admin.site.site_title = "MY Site"
urlpatterns = [
    #url(r'^admin/filebrowser/', site.urls),
    path('admin/', admin.site.urls),    
    path('projects/', include("requirement.urls")),'''