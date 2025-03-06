from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name='index'),
    path('travel/',travel,name='travel'),
    path('validate/',validate,name='validate'),
    path('entry_form/',entry_from,name='entry_form'),
    path('exit_form/',exit_form,name='exit_form'),
]