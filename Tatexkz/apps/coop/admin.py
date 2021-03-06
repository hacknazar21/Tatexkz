from django.contrib import admin

from Tatexkz.apps.coop.models import Coop, CoopSettings
from modeltranslation.admin import TranslationAdmin


class CoopAdmin(admin.ModelAdmin):
    list_display = ['name', 'tel',
                          'email', 'company', 'date']
    list_display_links = ['name', 'tel',
                          'email', 'company', 'date']
# Register your models here.
admin.site.register(Coop, CoopAdmin)
@admin.register(CoopSettings)
class CoopSettingsAdmin(TranslationAdmin):
    pass