from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import (HttpResponse, JsonResponse) 
from django.views.generic.base import TemplateView
from .models import (Synths, Reviews)
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Index(TemplateView):
    template_name = "index.html"

class SynthList(TemplateView):
    template_name = 'synths.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context["synths"] = Synths.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["synths"] = Synths.objects.all()
            context["header"] = "Synth Collection"
            return context

class NewSynth(CreateView):
    model = Synths
    fields = ['name', 'maker', 'year', 'img', 'info']
    template_name = 'new_synth.html'
    success_url = '/synths/'


class SynthInfo(DetailView):
    model = Synths
    template_name = 'synth_info.html'


class SynthUpdate(UpdateView):
    model = Synths
    fields = ['name', 'maker', 'year', 'img', 'info']
    template_name = 'synth_update.html'
    
    def get_success_url(self):
        return reverse('synth_info', kwargs={'pk': self.object.pk})


class SynthDelete(DeleteView):
    model = Synths
    template_name = 'synth_del_confirm.html'
    success_url = '/synths/'

class NewReview(CreateView):
    model = Reviews
    fields = ['review', 'synth']
    template_name = 'new_review.html'
    success_url = '/synths/'

class NewReviewFromNav(CreateView):
    model = Reviews
    fields = ['review', 'synth']
    template_name = 'nav_new_review.html'
    success_url = '/synths/'