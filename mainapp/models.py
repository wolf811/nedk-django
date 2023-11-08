from django.conf import settings
from django.db import models
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# from ckeditor.widgets import CKEditorWidget
from django.utils import timezone


class Chunk(models.Model):
    """class for making html chunks on pages"""
    title = models.CharField("Название вставки", max_length=100)
    code = models.CharField("Уникальный код",
                            max_length=64, default="CHUNK_CODE",)
    text = RichTextUploadingField("Текст вставки", null=True, blank=True,)
    picture = models.ImageField("Картинка", blank=True, null=True)
    created_date = models.DateTimeField("Дата создания", default=timezone.now)

    class Meta:
        verbose_name = "Вставка"
        verbose_name_plural = "Вставки"

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField("Наименование услуги", max_length=300)
    text = RichTextUploadingField("Описание")
    picture = models.ImageField("Картинка", blank=True, null=True)
    created_date = models.DateTimeField("Дата создания", default=timezone.now)
    ordering = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title


class Client(models.Model):
    client_name = models.CharField("Название", max_length=300)
    text = models.TextField("Описание", blank=True, null=True)
    logotype = models.ImageField("Картинка", blank=True, null=True)
    site = models.URLField("Адрес сайта", null=True, blank=True,)
    created_date = models.DateTimeField("Дата создания", default=timezone.now)
    ordering = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.client_name


class Portfolio(models.Model):
    service = models.ForeignKey(
        Service, verbose_name="Услуга", null=True, on_delete=models.SET_NULL)
    title = models.CharField("Название продукта", max_length=300)
    text = RichTextUploadingField("Описание")
    picture = models.ImageField("Картинка", blank=True, null=True)
    created_date = models.DateTimeField("Дата создания", default=timezone.now)
    ordering = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Продукт, услуга"
        verbose_name_plural = "Портфолио"

    def __str__(self):
        return self.title
