from django.urls import path
from . import views

#localhost:8000/njs

urlpatterns = [
    path('', views.njs_app, name='njsapp'),
]
