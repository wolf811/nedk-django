from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
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
    
class Contacts(models.Model):
    addr = models.TextField("Адрес",)
    addr_url = models.TextField("Ссылка на карту", null=True, blank=True,)
    phone = models.CharField("Телефон", max_length=100)
    email = models.EmailField("E-mail", max_length=254)
    driving_directions = models.TextField("Схема проезда", blank=True, null=True)
    created_date = models.DateTimeField("Дата создания", default=timezone.now)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.addr


class Feedback(models.Model):
    service = models.ForeignKey(
        Service,
        verbose_name="Услуга",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    subject = models.CharField('Имя', max_length=255,  null=True, blank=True)
    phone = models.CharField('Телефон', max_length=255, null=True, blank=True)
    email = models.EmailField('E-mail', max_length=255,)
    content = models.TextField('Текст запроса')
    created_date = models.DateTimeField('Дата отправки', auto_now_add=True,)
    ip_address = models.GenericIPAddressField('IP отправителя', blank=True, null=True)
    # user = models.ForeignKey(User, verbose_name='Пользователь',
    #                          on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-created_date']
        db_table = 'app_feedback'

    def __str__(self):
        return f'Вам письмо от {self.email}'
