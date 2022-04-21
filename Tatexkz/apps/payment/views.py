import json
import re
from django.shortcuts import render
from Tatexkz.apps.order.views import calcPromo, calcTariff

from Tatexkz.apps.payment.models import Order
from Tatexkz.apps.payment.views import calcTariff
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def payment(request):
    if request.method == "POST":
        weight = float(request.POST.get(
            'weight', 'Не найдено').replace(' (кг)', ''))
        Order(
            typePackage=request.POST.get('type', ''),
            fromCity=request.POST.get('from', ''),
            whereCity=request.POST.get('where', ''),
            weight=weight,
            fromCountry=request.POST.get('from_country', ''),
            whereCountry=request.POST.get('where_country', ''),
            length=request.POST.get('length', 0),
            width=request.POST.get('width', 0),
            height=request.POST.get('height', 0),
            sendersAddress=request.POST.get('sendersAddress', ''),
            recipientAddress=request.POST.get('recipientAddress', ''),
            postIndexSender=request.POST.get('postIndexSender', ''),
            postIndexRecipient=request.POST.get('postIndexRecipient', ''),
            dataSend=request.POST.get('dataSend', ''),
            sendersName=request.POST.get('sendersName', ''),
            sendersTel=request.POST.get('full_sendersTel', ''),
            recipientName=request.POST.get('recipientName', ''),
            recipientTel=request.POST.get('full_recipientTel', ''),
            email=request.POST.get('email', ''),
            comment=request.POST.get('comment', ''),
            printNeed=request.POST.get('print'),
        ).save()
        promo = request.POST.get('promo', '')

        promoResp = calcPromo(promo)
        calculatedTariff = calcTariff(
            request.POST.get('type', ''),
            request.POST.get('from', ''),
            request.POST.get('where', ''),
            request.POST.get('from_country', ''),
            request.POST.get('where_country', ''),
            weight)
        if promoResp['percent'] > -1:
            calculatedTariff = calculatedTariff - \
                calculatedTariff*(promoResp['percent']/100)
        return render(
            request, 'payment/payment.html', {
                'error': False,
                'email': request.POST.get('email', ''),
                'price': calculatedTariff
            }
        )
    else:
        return render(
            request, 'payment/payment.html', {
                'error': False,
                'email': "test@ad.com",
                'price': 500,
                'errorText': 'Упс. Данная страница недоступна'
            }
        )
