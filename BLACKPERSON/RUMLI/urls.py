from django.urls import path
from . import views

urlpatterns = [
    path('', views.szohi, name='home-page'),
]