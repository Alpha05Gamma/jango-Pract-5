from django.contrib import admin
from .models import Enemy, Boss, NPC, Item, Weapon

# Register your models here.

class EnemyAdmin(admin.ModelAdmin):
    list_display = ('name', 'health', 'runes', 'loot')

class BossAdmin(admin.ModelAdmin):
    list_display = ('Enemy', 'description')

class NPCAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cost')

class WeaponAdmin(admin.ModelAdmin):
    list_display = ('Item', 'damage_types', 'location', 'skill')

admin.site.register(Enemy, EnemyAdmin)
admin.site.register(Boss, BossAdmin)
admin.site.register(NPC, NPCAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Weapon, WeaponAdmin)