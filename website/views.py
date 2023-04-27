from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import Offer, BlockWithVideo, Trainer, Offer, ContactData, PriceList

class HomeView(TemplateView):
    template_name = 'home.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["offers"] = Offer.active_objects.all()
        context["blocks_with_video"] = BlockWithVideo.active_objects.all()
        context["trainers"] = Trainer.active_objects.all()
        context["price_list"] = PriceList.active_objects.all()
        context["contact"] = ContactData.active_objects.all()
        return context