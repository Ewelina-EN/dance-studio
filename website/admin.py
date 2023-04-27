from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Offer, BlockWithVideo, Trainer, Offer, ContactData, PriceList

admin.site.register(Offer)
admin.site.register(BlockWithVideo)
admin.site.register(Trainer)
admin.site.register(ContactData)
admin.site.register(PriceList)
