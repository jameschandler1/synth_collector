from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
# Create your views here.


# regular views
# class Home(View):
    
#     def get(self, request):
#         return HttpResponse("homepage")

# class About(View):

#     def get(self, request):
#         return HttpResponse("aboutpage")

# class Index(View):

#     def get(self, request):
#         return HttpResponse("indexpage")


#template views

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Index(TemplateView):
    template_name = "index.html"


class Synth:
    def __init__(self, name, maker, year, img, info):
        self.name = name
        self.maker = maker
        self.year = year
        self.img = img
        self.info = info

synths = [
    Synth('Mono/Poly','KORG', 1981, 'https://www.amazona.de/wp-content/uploads/2010/06/korg-monopoly-full-3.jpg', 'The Mono/Poly (MP-4) is a 44 key "mono-polyphonic" analog synthesizer made by Korg from 1981 to 1984. It has four voltage-controlled oscillators (VCOs), 4-pole, self-oscillating low pass filter (LPF), wide modulation capabilities and pseudo-polyphony.'),
    Synth('Mono/Poly','KORG', 1981, 'https://www.amazona.de/wp-content/uploads/2010/06/korg-monopoly-full-3.jpg', 'The Mono/Poly (MP-4) is a 44 key "mono-polyphonic" analog synthesizer made by Korg from 1981 to 1984. It has four voltage-controlled oscillators (VCOs), 4-pole, self-oscillating low pass filter (LPF), wide modulation capabilities and pseudo-polyphony.'),
    Synth('Mono/Poly','KORG', 1981, 'https://www.amazona.de/wp-content/uploads/2010/06/korg-monopoly-full-3.jpg', 'The Mono/Poly (MP-4) is a 44 key "mono-polyphonic" analog synthesizer made by Korg from 1981 to 1984. It has four voltage-controlled oscillators (VCOs), 4-pole, self-oscillating low pass filter (LPF), wide modulation capabilities and pseudo-polyphony.'),
]

class SynthList(TemplateView):
    template_name = 'synths.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["synths"] = synths
        return context
