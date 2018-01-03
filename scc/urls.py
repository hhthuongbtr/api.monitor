from django.conf.urls import url
from scc import views

urlpatterns = [

    url(r'^$', views.Scc().routing),
]

