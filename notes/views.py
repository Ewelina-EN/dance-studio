from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from .models import Note

class NoteListView(ListView):
    model = Note
    template_name = 'note_list.html'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'
    context_object_name = 'note'

class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'note_form.html'
    success_url = reverse_lazy('note_list')

class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'note_form.html'
    success_url = reverse_lazy('note_list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_delete.html'
    success_url = reverse_lazy('note_list')

class OfferHeaderView(TemplateView):
    template_name = 'dance_studio.html'  