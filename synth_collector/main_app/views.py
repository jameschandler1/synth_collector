
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View # <- View class to handle requests
from django.views.generic.base import TemplateView
from .models import (Synth, Comment)
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Index(TemplateView):
    template_name = "index.html"

@method_decorator(login_required, name='dispatch')
class SynthList(TemplateView):
    template_name = 'synths.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context["synths"] = Synth.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
            return context
        else:
            context["synths"] = Synth.objects.all()
            context["header"] = "Synth Collection"
            return context
    
@method_decorator(login_required, name='dispatch')
class NewSynth(CreateView):
    model = Synth
    template_name = 'new_synth.html'
    fields = ['name', 'maker', 'year', 'img', 'info']
    success_url = '/synths/'

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super(NewSynth, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class SynthInfo(DetailView):
    model = Synth
    template_name = 'synth_info.html'

@method_decorator(login_required, name='dispatch')
class SynthUpdate(UpdateView):
    model = Synth
    fields = ['name', 'maker', 'year', 'img', 'info']
    template_name = 'synth_update.html'
    
    def get_success_url(self):
        return reverse('synth_info', kwargs={'pk': self.object.pk})

    

@method_decorator(login_required, name='dispatch')
class SynthDelete(DeleteView):
    model = Synth
    template_name = 'synth_del_confirm.html'
    success_url = '/synths/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_body = self.request.GET.get('comment_body')
        if comment_body != None:
            return print('no Comments')
        else:
            context["body"] = Comment.objects.all().filter(comment_body=comment_body)
            return context
    
class SignUp(View):
    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'registration/signup.html', context)

@method_decorator(login_required, name='dispatch')
class MakeComment(CreateView):
    model = Comment
    fields = ['comment_body']
    template_name = 'new_comment.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MakeComment, self).form_valid(form)

    def get_success_url(self):
        return reverse('synth_info', kwargs={'pk': self.object.sfk })


@method_decorator(login_required, name='dispatch')
class DelComment(DeleteView):
    template_name = 'del_review.html'
    model = Comment
    success_url = '/synths/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DelComment, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditComment(UpdateView):
    model = Comment
    template_name = 'edit_review.html'
    fields = ['body']
    success_url = '/synths/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EditComment, self).form_valid(form)


    
