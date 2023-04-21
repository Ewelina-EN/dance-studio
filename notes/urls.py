from django.urls import path
from .views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView, NoteDetailView, OfferHeaderView

urlpatterns = [
    path('', NoteListView.as_view(), name='note_list'),
    path('add/', NoteCreateView.as_view(), name='note_add'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note_details'),
    path('<int:pk>/edit/', NoteUpdateView.as_view(), name='note_edit'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
    path('studio/', OfferHeaderView.as_view(), name='dance_studio'),
]