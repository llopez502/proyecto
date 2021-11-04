from django.urls.base import reverse
from .models import Cine, Sala, Fila, Pelicula
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView)


class cineListView(ListView):
    model = Cine
    template_name = 'cine_list.html'

class cineCreateView(CreateView):
    model = Cine
    template_name = 'cine_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('Cine_list')

class cineUpdateView(UpdateView):
    model = Cine
    template_name = 'cine_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('Cine_list')

class cineDeleteView(DeleteView):
    model = Cine
    template_name = 'Cine_delete.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('Cine_list')