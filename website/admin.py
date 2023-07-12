from django.contrib import admin

# Register your models here.
from .models import (
    Offer,
    BlockWithVideo,
    Trainer,
    Offer,
    ContactData,
    PriceList,
    ScheduleItem,
    HeaderContent,
    Client,
)

admin.site.register(Offer)
admin.site.register(BlockWithVideo)
admin.site.register(Trainer)
admin.site.register(ContactData)
admin.site.register(PriceList)
admin.site.register(HeaderContent)


@admin.register(ScheduleItem)
class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ["title", "week_day", "start_time", "end_time", "is_active"]
    list_filter = ["week_day", "is_active"]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "activity", "created_at"]
