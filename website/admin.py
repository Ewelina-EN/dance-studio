from django.contrib import admin

# Register your models here.
from .models import Offer, BlockWithVideo, Trainer, Offer, ContactData, PriceList, ScheduleItem

admin.site.register(Offer)
admin.site.register(BlockWithVideo)
admin.site.register(Trainer)
admin.site.register(ContactData)
admin.site.register(PriceList)

@admin.register(ScheduleItem)
class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ["title", "week_day", "start_time", "end_time", "is_active"]
    list_filter = ["week_day", "is_active"]

