from django.views import generic
from django.urls import reverse_lazy
from .models import Greeting

class IndexView(generic.ListView):
  template_name = 'greetings/index.html'
  context_object_name = 'greeting_list'

  def get_queryset(self):
    """Return all the greetings."""
    return Greeting.objects.all()

class CreateView(generic.edit.CreateView):
  template_name = 'greetings/create.html'
  model = Greeting
  fields = ['message']
  success_url = reverse_lazy('greetings:index')

class UpdateView(generic.edit.UpdateView):
    template_name = 'greetings/update.html'
    model = Greeting
    fields = ['message']
    success_url = reverse_lazy('greetings:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'greetings/delete.html'
    model = Greeting
    success_url = reverse_lazy('greetings:index')

