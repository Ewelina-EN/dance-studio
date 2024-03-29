import os
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from .views import HomeView, RulesView, PrivacyPolicyView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("regulamin/", RulesView.as_view(), name="rules"),
    path("polityka-prywatnosci/", PrivacyPolicyView.as_view(), name="privacy_policy"),
]
if not os.environ.get("IS_PRODUCTION"):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
