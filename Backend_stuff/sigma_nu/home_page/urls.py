from django.conf.urls import url
from . import views

urlpatterns = [

    #home page and everythin
    url(r'^$', views.index, name = 'index')
    
]
