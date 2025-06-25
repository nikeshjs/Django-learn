from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Welcome to my django learning series. You are at a home page right now.")
    return render(request, 'website/index.html')

def about(request):
    #return HttpResponse("Welcome to my django learning series. You are at about page right now.")
    return render(request, 'website/about.html')

def contact(request):
    return HttpResponse("Welcome to my django learning series. You are at contact page right now.")

