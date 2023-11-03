from django.conf import settings
from django.db import models
from django.utils import timezone


class Service(models.Model):
    title = models.CharField(
        verbose_name="Наименование услуги", max_length=300)
    text = models.TextField(verbose_name="Описание")
    created_date = models.DateTimeField(
        verbose_name="Дата создания", default=timezone.now)
    published_date = models.DateTimeField(
        verbose_name="Дата публикации", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
