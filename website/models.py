from django.db import models

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
    
class BasicModel(models.Model):
    # Ignore!
    title = models.CharField(max_length=255)
    is_active = models.BooleanField("aktywne?", default=True, help_text="Czy to ma się wyświetlać na stronie?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self) -> str:
        return self.title

    class Meta:
        abstract = True
    # /Ignore
    
class Offer(BasicModel):
    content = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="offer")

class BlockWithVideo(BasicModel):
    content = models.CharField(max_length=255)
    # content_1 = models.CharField(max_length=255)
    video_iframe_src_url_1 = models.URLField()
    video_iframe_src_url_2 = models.URLField()
    video_iframe_src_url_3 = models.URLField()

class Trainer(BasicModel):
    content = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="trainers")

class PriceList(BasicModel):
    content_1 = models.CharField(max_length=255)
    content_2 = models.CharField(max_length=255)
    content_3 = models.CharField(max_length=255)
    content_4 = models.CharField(max_length=255)
    price = models.FloatField("cena")

class ContactData(BasicModel):
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    facebook = models.URLField()
    instagram = models.URLField()

class WeekDay(BasicModel):
    @property
    def schedule_items(self):
        return ScheduleItem.active_objects.filter(week_day=self)

class ScheduleItem(BasicModel):
    week_day = models.ForeignKey(WeekDay,on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    instructor = models.CharField(max_length=255)