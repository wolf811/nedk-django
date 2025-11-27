from django.contrib import admin

# from mptt.admin import DraggableMPTTAdmin
from mainapp.models import *


@admin.register(Chunk)
class ChunkAdmin(admin.ModelAdmin):
    list_display = ['title', 'code', 'created_date']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'ordering']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'site', 'created_date', 'ordering']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'service', 'created_date', 'ordering']


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['addr', 'phone', 'email', 'created_date',]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Админ-панель модели профиля
    """
    list_display = ('email', 'phone', 'service', 'ip_address',)
    list_display_links = ('email', 'ip_address')
