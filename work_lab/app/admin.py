from django.contrib import admin
from .models import *

# Register your models here.


class BarracksAdmin(admin.ModelAdmin):
    list_display = ['number', 'capacity', 'purpose']
    search_fields = ['number', 'capacity', 'purpose']


class WeaponAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'number']
    search_fields = ['name', 'brand', 'number']


class MilitaryAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'patronymic', 'barracks_number', 'received_weapon']
    search_fields = ['surname']


admin.site.register(Barracks, BarracksAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Military, MilitaryAdmin)
