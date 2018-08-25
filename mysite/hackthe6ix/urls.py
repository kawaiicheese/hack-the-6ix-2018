from django.urls import path

from . import views

app_name = 'hackthe6ix'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name="register"),
    path('login/', views.index, name="login"),
    path('verify/', views.verify, name="verify"),
]