from django.contrib import admin

from Tatexkz.apps.promo.models import Promo


class PromoAdmin(admin.ModelAdmin):
    list_display = ['promo', 'datefrom', 'dateto', 'percent']


# Register your models here.
admin.site.register(Promo, PromoAdmin)
