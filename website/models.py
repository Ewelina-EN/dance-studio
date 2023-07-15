from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BasicModel(models.Model):
    # Ignore!
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(
        "aktywne?", default=True, help_text="Czy to ma się wyświetlać na stronie?"
    )
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
    content_extended = models.CharField(max_length=255)
    video_iframe_src_url_1 = models.URLField()
    video_iframe_src_url_2 = models.URLField()
    video_iframe_src_url_3 = models.URLField()
    video_iframe_src_url_4 = models.URLField()
    content_button = models.CharField(max_length=100, blank=True)
    button = models.CharField(max_length=50, blank=True)


class Trainer(BasicModel):
    content = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="trainers")


class PriceList(BasicModel):
    content_1 = models.CharField(max_length=255)
    content_2 = models.CharField(max_length=255)
    content_3 = models.CharField(max_length=255)
    content_4 = models.CharField(max_length=255)
    price = models.CharField(max_length=255)


class ContactData(BasicModel):
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    facebook = models.URLField()
    instagram = models.URLField()
    youtube = models.URLField()


class WeekDay(BasicModel):
    @property
    def schedule_items(self):
        return ScheduleItem.active_objects.filter(week_day=self)


class ScheduleItem(BasicModel):
    week_day = models.ForeignKey(WeekDay, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    instructor = models.CharField(max_length=255)

    class Meta:
        ordering = ["start_time"]


class HeaderContent(BasicModel):
    content = models.CharField(max_length=255)


class Client(models.Model):
    choices = (
        (None, "Wybierz"),
        ("Strip Dance", "Strip Dance"),
        ("High Heels", "High Heels"),
        ("Strip Acro", "Strip Acro"),
        ("Female Dance", "Female Dance"),
    )

    name = models.CharField("Imię", max_length=255)
    phone = models.CharField("Numer telefonu", max_length=255)
    email = models.EmailField("Email", max_length=255)
    activity = models.CharField("Rodzaj zajęć", choices=choices, max_length=255)
    consent = models.BooleanField("Zgoda na przetwarzanie danych")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} {self.phone} {self.email}"
