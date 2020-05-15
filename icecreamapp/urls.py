from django.urls import path
from django.conf.urls import include
from icecreamapp import views
from .views import flavor_list

app_name = "icecreamapp"

urlpatterns = [
    path('', flavor_list, name='flavor_list'),
]
