from django.contrib import admin
from django.utils.html import format_html

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['status', 'trackcode', 'sendersName', 'sendersTel',
                    'sendersAddress', 'recipientName', 'recipientAddress', 'applyButton', 'downloadDocs']
    search_fields = ['sendersName', 'sendersTel',
                    'sendersAddress', 'recipientName', 'recipientAddress']

    def applyButton(self, obj):
        print(obj.shipmentDate)
        if obj.apply:
            return format_html(
                """
                    <button class = "button dhl-button" type = "submit" disabled="true"> Отправлено </button >                
                """, obj.sendersName,
                obj.sendersTel,
                obj.sendersAddress,
                obj.recipientAddress,
                obj.weight,
                obj.id,
                obj.email,
                obj.recipientName,
                obj.recipientTel,
                obj.postIndexSender,
                obj.postIndexRecipient,
                obj.fromCity,
                obj.whereCity,
                obj.fromCountry,
                obj.whereCountry,
                obj.dataSend,
                obj.status
            )
        return format_html(
            """
                    <input type = "hidden" name = "sendersName"  value = "{0}" >
                    <input type = "hidden" name = "sendersTel"  value = "{1}" >
                    <input type = "hidden" name = "sendersAddress"  value = "{2}" >
                    <input type = "hidden" name = "recipientAddress"  value = "{3}" >
                    <input type = "hidden" name = "weight"  value = "{4}" >
                    <input type = "hidden" name = "id"  value = "{5}" >
                    <input type = "hidden" name = "email"  value = "{6}" >
                    <input type = "hidden" name = "recipientName"  value = "{7}" >
                    <input type = "hidden" name = "recipientTel"  value = "{8}" >
                    <input type = "hidden" name = "postIndexSender"  value = "{9}" >
                    <input type = "hidden" name = "postIndexRecipient"  value = "{10}" >
                    <input type = "hidden" name = "fromCity"  value = "{11}" >
                    <input type = "hidden" name = "whereCity"  value = "{12}" >
                    <input type = "hidden" name = "fromCountry"  value = "{13}" >
                    <input type = "hidden" name = "whereCountry"  value = "{14}" >
                    <input type = "hidden" name = "dateSend"  value = "{15}" >
                    <input type = "hidden" name = "type"  value = "{16}" >
                    <input type = "hidden" name = "shipmentTimeMin"  value = "{17}" >
                    <input type = "hidden" name = "shipmentTimeMax"  value = "{18}" >
                    <button class = "button dhl-button"> Подтвердить </button >
                """, obj.sendersName,
            obj.sendersTel,
            obj.sendersAddress,
            obj.recipientAddress,
            obj.weight,
            obj.id,
            obj.email,
            obj.recipientName,
            obj.recipientTel,
            obj.postIndexSender,
            obj.postIndexRecipient,
            obj.fromCity,
            obj.whereCity,
            obj.fromCountry,
            obj.whereCountry,
            obj.dataSend,
            obj.typePackage,
            obj.shipmentDate,
            obj.shipmentDateFuture)

    def downloadDocs(self, obj):
        if obj.apply:
            return format_html(
                """ 
                    <a target="_blank" class="button" href="/static/files/{0}/Receipt.pdf"> Квитанция </a>
                    <br/>
                    <br/>
                    <a  class="button" target="_blank" href="/static/files/{0}/Накладная.pdf"> Накладная </a>
                """, obj.trackcode
            )
        else:
            return format_html(
                """ 
                    <button class="button" disabled="true"> Квитанция </button>
                    <br/>
                    <button class="button" disabled="true"> Накладная </button>
                """
            )
    applyButton.short_description = 'Отправить в DHL'
    downloadDocs.short_description = 'Скачать'
    list_display_links = ['sendersName', 'trackcode', 'sendersTel',
                          'sendersAddress', 'recipientName', 'recipientAddress']

    class Media:
        js = (
            'js/admin-form.js',   # app static folder
        )


admin.site.site_header = 'Администрирование Tatex.kz'
admin.site.register(Order, OrderAdmin)
