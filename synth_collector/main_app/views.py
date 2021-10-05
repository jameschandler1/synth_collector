from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse 
# Create your views here.

class Home(View):
    
    def get(self, request):
        return HttpResponse("homepage")

class About(View):

    def get(self, request):
        return HttpResponse("aboutpage")

class Index(View):

    def get(self, request):
        return HttpResponse("indexpage")