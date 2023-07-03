from django.urls import path
from .views import  home

app_name="ps_test"

urlpatterns = [
    path('', home, name="home"),
]