from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
# Create your views here.


# regular views
class Home(View):
    
    def get(self, request):
        return HttpResponse("homepage")

class About(View):

    def get(self, request):
        return HttpResponse("aboutpage")

class Index(View):

    def get(self, request):
        return HttpResponse("indexpage")


#template views

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Index(TemplateView):
    template_name = "index.html"