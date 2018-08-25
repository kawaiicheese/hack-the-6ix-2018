from django.urls import path

from . import views

app_name = 'hackthe6ix'
urlpatterns = [
    path('', views.index, name='index'),
]