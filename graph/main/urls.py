from django.urls import path
from . import views

from django.urls import path
from main.views import run_script


urlpatterns = [
        path('', views.index),
        path('run_script/', run_script, name='run_script'),
]

