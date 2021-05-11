from django.urls import path
from staff import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url


#url.site.site_title = "Technology Innovation Group"
#admin.site.site_header = "Technology Innovation Group Administrator"
#admin.site.site_title = "Technology Innovation Group"
urlpatterns = [
    path("", views.requirement_req, name="requirement_req"),
]