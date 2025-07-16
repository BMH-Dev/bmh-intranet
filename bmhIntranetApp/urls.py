from django.urls import path
from . import views

app_name = 'bmhIntranetApp'

urlpatterns = [
    path('', views.demo, name='demo'),
]