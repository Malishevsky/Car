from django.contrib import admin

from .models import Auto,Transmission,Engine

@admin.register(Auto)
class AdminAuto(admin.ModelAdmin):
    list_display = ('firm','model','color','volume','engine','transmission','price')

@admin.register(Transmission)
class AdminTransmission(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Engine)
class AdminEngine(admin.ModelAdmin):
    list_display = ('name',)
