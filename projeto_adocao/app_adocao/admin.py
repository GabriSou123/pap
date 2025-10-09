from django.contrib import admin
from .models import Animal
from .models import PerfilUtilizador

admin.site.register(Animal)
admin.site.register(PerfilUtilizador)


class AnimalAdmin(admin.ModelAdmin):
    search_fields = ('nome',)


