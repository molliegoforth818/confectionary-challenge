from django.urls import path
from django.conf.urls import include
from icecreamapp import views
from .views import *

app_name = "icecreamapp"

urlpatterns = [
    path('', variety_list, name='variety_list'),
    path('variety/form/', variety_form, name='variety_form'),

]
