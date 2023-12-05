from typing import Any
from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from cardquest.models import PokemonCard, Trainer

class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainers.html'
    paginate_by = 15

class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context