from django.shortcuts import render

# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import TemplateView, CreateView
from .models import (
    Offer,
    BlockWithVideo,
    Trainer,
    Offer,
    ContactData,
    PriceList,
    WeekDay,
    HeaderContent,
)
from .forms import ClientForm


class HomeView(SuccessMessageMixin, CreateView):
    template_name = "home.html"
    form_class = ClientForm
    success_url = "/#contact_form"
    success_message = "Dziękujemy za kontakt. Odezwiemy się wkrótce."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["offers"] = Offer.active_objects.all()
        context["blocks_with_video"] = BlockWithVideo.active_objects.all()
        context["trainers"] = Trainer.active_objects.all()
        context["price_list"] = PriceList.active_objects.all()
        context["contact"] = ContactData.active_objects.first()
        context["weekdays"] = WeekDay.active_objects.all()
        context["header_content"] = HeaderContent.active_objects.all()
        return context


class RulesView(TemplateView):
    template_name = "rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = ContactData.active_objects.first()
        return context


class PrivacyPolicyView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = ContactData.active_objects.first()
        return context

    template_name = "privacy-policy.html"
