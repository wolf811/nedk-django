from django.contrib import admin
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
