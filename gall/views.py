from django.template import context
from django.views.generic import View, TemplateView, DetailView, ListView

from . models import Flower

class HomeView(ListView):
    template_name = 'home.html'
    model = Flower
    context_object_name = 'flowers'

class FlowerDetailView(DetailView):
    template_name = 'detail.html'
    model = Flower
    context_object_name = 'flower'