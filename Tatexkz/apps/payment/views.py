import json
import re
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from Tatexkz.apps.order.views import calcPromo, calcTariff

from Tatexkz.apps.payment.models import Order
from Tatexkz.apps.payment.views import calcTariff
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage



@csrf_exempt
def payment(request):

    if request.method == "POST":
        weight = float(request.POST.get(
            'weight', 'Не найдено').replace(' (кг)', ''))
        postIndexSender = ''.join(i for i in request.POST.get('postIndexSender', '') if not i.isalpha())
        postIndexRecipient = ''.join(i for i in request.POST.get('postIndexRecipient', '') if not i.isalpha())

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
            postIndexSender=postIndexSender,
            postIndexRecipient=postIndexRecipient,
            dataSend=request.POST.get('dataSend', ''),
            sendersName=request.POST.get('sendersName', ''),
            sendersTel=request.POST.get('full_sendersTel', ''),
            recipientName=request.POST.get('recipientName', ''),
            recipientTel=request.POST.get('full_recipientTel', ''),
            email=request.POST.get('email', ''),
            comment=request.POST.get('comment', ''),
            instruction=request.POST.get('instruction', ''),
            printNeed=request.POST.get('print')
        ).save()

        person = Order.objects.latest('id')
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
        msg = ''
        msg += 'Вес: ' + str(weight) + '\n'
        msg += 'Город отправителя: ' + request.POST.get('from', '') + '\n'
        msg += 'Адрес отправителя: ' + request.POST.get('sendersAddress', '') + '\n'
        msg += 'Почтовый индекс отправителя: ' + postIndexSender + '\n'
        msg += 'Город получателя: ' + request.POST.get('where', '') + '\n'
        msg += 'Адрес получателя: ' + request.POST.get('recipientAddress', '') + '\n'
        msg += 'Почтовый индекс получателя: ' + postIndexRecipient + '\n'
        msg += 'Дата забора: ' + request.POST.get('dataSend', '') + '\n'
        msg += 'Имя отправителя: ' + request.POST.get('sendersName', '') + '\n'
        msg += 'Телефон отправителя: ' + request.POST.get('full_sendersTel', '') + '\n'
        msg += 'Имя получателя: ' + request.POST.get('recipientName', '') + '\n'
        msg += 'Телефон получателя: ' + request.POST.get('full_recipientTel', '') + '\n'
        msg += 'К оплате: ' + str(calculatedTariff) + '\n'
        msg += 'Вид груза: ' + request.POST.get('type', '') + '\n'
        msg += 'Комментарий для курьера: ' + request.POST.get('instruction', '') + '\n'
        msg += 'Подробное содержимое груза: ' + request.POST.get('comment', '') + '\n'
        message = EmailMessage(
            'Создана новая заявка Tatex.kz',
            msg,
            to=['info@tatex.kz']
        )
        message.send(fail_silently=False)
        return render(
            request, 'payment/payment.html', {
                'error': False,
                'email': request.POST.get('email', ''),
                'price': calculatedTariff, #1
                'ID': person.id + 1000000,
                'ids': person.id
            }
        )
    else:
        return render(
            request, 'payment/payment.html', {
                'error': False,
                'email': "test@ad.com",
                'price': 1,
                'errorText': 'Упс. Данная страница недоступна',
                'ID': '109600746892'
            }
        )
@csrf_exempt
def createorder(request):
    if request.method == "POST":
        person_id = request.POST.get('id', -1)
        if(person_id != -1):
            payPerson = Order.objects.get(id=person_id)
            payPerson.isPay = True
            payPerson.save()
    else:
        raise Http404('Извините, страница не найдена. No Found :(')