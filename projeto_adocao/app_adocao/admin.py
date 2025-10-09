from django.contrib import admin
from .models import Animal

admin.site.register(Animal)

class AnimalAdmin(admin.ModelAdmin):
    search_fields = ('nome',)