from django.urls import path
from .views import HomeView

urlpatterns = [
    path('studio/', HomeView.as_view(), name='dance_studio'),
]