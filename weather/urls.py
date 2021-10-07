from django.urls import path
from django.urls import URLPattern 
from . import views 

urlpatterns = [
    path('',views.index, name = 'index')
]