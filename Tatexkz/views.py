import base64
from datetime import datetime
import json
from re import sub
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import requests
from bs4 import BeautifulSoup as BS
import xml.etree.ElementTree as ET
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from Tatexkz.apps.payment.models import Order
from transliterate import translit
from pathlib import Path
from django.core.mail import EmailMessage

countiesRoot = ET.parse('static/files/counties-codes.xml')
countriesCodes = {}
for country in countiesRoot.iter('country'):
    for name in country.iter('name'):
        for alpha2 in country.iter('alpha2'):
            countriesCodes[name.text] = alpha2.text


def tracking(request):
    if(request.GET):
        try:
            trackcode = request.GET.get('trackcode', '')
            try:
                person = Order.objects.get(trackcode=trackcode)
            except Order.DoesNotExist:
                return redirect('/#popup_error')

            country = person.whereCountry
            city = person.whereCity
            address = person.recipientAddress
            addressStr = country + ',  г. ' + city + ', ' + address
            dateApply = person.date
            tree = ET.parse('static/files/trackReq.xml')
            root = tree.getroot()
            for AWBNumber in root.iter('AWBNumber'):
                AWBNumber.text = trackcode
            for MessageTime in root.iter('MessageTime'):
                MessageTime.text = datetime.utcnow().isoformat()
            tree.write('static/files/trackReq.xml', 'UTF-8')
            with open('static/files/trackReq.xml') as inputfile:
                xml_file = inputfile.read()
            response = requests.post(
                'http://xmlpi-ea.dhl.com/XMLShippingServlet?isUTF8Support=true', data=xml_file)

            respRoot = ET.fromstring(response.text)
            events = []
            dateShipment = ''
            for ShipmentDate in respRoot.iter('ShipmentDate'):
                dateShipment = datetime.fromisoformat(
                    ShipmentDate.text).strftime("%d.%m.%Y")
            print(response.text)
            for ShipmentEvent in respRoot.iter('ShipmentEvent'):
                event = {}
                for Date in ShipmentEvent.iter('Date'):
                    event['date'] = Date.text
                for Time in ShipmentEvent.iter('Time'):
                    event['time'] = Time.text
                for ServiceEvent in ShipmentEvent.iter('ServiceEvent'):
                    for Description in ServiceEvent.iter('Description'):
                        event['description'] = Description.text.replace(
                            '<>', '')
                    for EventCode in ServiceEvent.iter('EventCode'):
                        if EventCode.text == 'PU' or EventCode.text == 'FD' or EventCode.text == 'DF':
                            event['code'] = '_green-indicator'
                        elif EventCode.text == 'CS' or EventCode.text == 'OH' or EventCode.text == 'AF':
                            event['code'] = '_yellow-indicator'
                        elif EventCode.text == 'MS':
                            event['code'] = '_red-indicator'
                        else:
                            event['code'] = '_no-indicator'
                events.append(event)

        except ValueError:
            return redirect('/#popup_error')

    return render(
        request, 'tracking/tracking.html', {
            'trackcode': trackcode,
            'dateShipment': dateShipment,
            'addressStr': addressStr,
            'dateApply': dateApply,
            'events': events
        }
    )


def oferta(request):
    return render(
        request, 'oferta/index.html'
    )


def privacy(request):
    return render(
        request, 'privacy/index.html'
    )


@csrf_exempt
def dhl(request):
    if request.method == "POST":

        jsonReq = json.loads(request.body.decode('utf-8'))
        weight = jsonReq.get('weight', '')
        height = jsonReq.get('height', '1')
        length = jsonReq.get('length', '1')
        width = jsonReq.get('width', '1')
        email = jsonReq.get('email', '')
        type = jsonReq.get('type', '')
        pickupDate = jsonReq.get('dateSend', '').split('/')
        dateSend = datetime.now()
        dateSend = dateSend.strftime('%Y-%m-%d')
        postIndexSender = jsonReq.get('postIndexSender', '000000')
        postIndexRecipient = jsonReq.get('postIndexRecipient', '000000')
        sendersName = translit(jsonReq.get(
            'sendersName', ''), language_code='ru', reversed=True)
        sendersTel = jsonReq.get('sendersTel', '').replace(
            ' (', '').replace(') ', '').replace('-', '')
        sendersAddress = translit(jsonReq.get(
            'sendersAddress', ''), language_code='ru', reversed=True)
        recipientAddress = translit(jsonReq.get(
            'recipientAddress', ''), language_code='ru', reversed=True)
        recipientTel = jsonReq.get(
            'recipientTel', '').replace(
            ' (', '').replace(') ', '').replace('-', '')
        recipientName = translit(jsonReq.get(
            'recipientName', ''), language_code='ru', reversed=True)
        fromCity = translit(jsonReq.get(
            'fromCity', ''), language_code='ru', reversed=True)
        whereCity = translit(jsonReq.get(
            'whereCity', ''), language_code='ru', reversed=True)
        fromCountry = translit(jsonReq.get(
            'fromCountry', ''), language_code='ru', reversed=True)
        whereCountry = translit(jsonReq.get(
            'whereCountry', ''), language_code='ru', reversed=True)
        timeMin = jsonReq.get('shipmentTimeMin', '')
        timeMax = jsonReq.get('shipmentTimeMax', '')
        
        fromCountryCode = countriesCodes[jsonReq.get('fromCountry', '')]
        whereCountryCode = countriesCodes[jsonReq.get('whereCountry', '')]

        if type == 'document':
            typeCode = 'DC'
            if float(weight) <= 0.3:
                GlobalProductCodeType = 'X'
            else:
                GlobalProductCodeType = 'D'
        else:
            typeCode = 'YP'
            GlobalProductCodeType = 'P'
        accountNumber = '376165440'
        if fromCountryCode == 'KZ':
            accountNumber = '376165440'
        else:
            accountNumber = '967710648'
        if whereCountry == fromCountry:
            GlobalProductCodeType = 'N'

        personID = jsonReq.get('id', 0)
        tree = ET.parse('static/files/req.xml')
        root = tree.getroot()
        i = 0
        for MessageTime in root.iter('MessageTime'):
            MessageTime.text = datetime.utcnow().isoformat()
        for weightXML in root.iter('Weight'):
            weightXML.text = weight
        for heightXML in root.iter('Height'):
            heightXML.text = height
        for lengthXML in root.iter('Depth'):
            lengthXML.text = length
        for PersonName in root.iter('PersonName'):
            if not i:
                PersonName.text = recipientName
            else:
                PersonName.text =  sendersName
                i = 0
                break
            i += 1
        for CompanyName in root.iter('CompanyName'):
            if not i:
                CompanyName.text = recipientName
            else:
                CompanyName.text =  sendersName
                i = 0
                break
            i += 1
        for AddressLine1 in root.iter('AddressLine1'):
            if not i:
                AddressLine1.text = recipientAddress
            else:
                AddressLine1.text =  sendersAddress
                i = 0
                break
            i += 1
        for PhoneNumber in root.iter('PhoneNumber'):
            if not i:
                PhoneNumber.text =  recipientTel
            else:
                PhoneNumber.text =  sendersTel
                i = 0
                break
            i += 1
        for PostalCode in root.iter('PostalCode'):
            if not i:
                PostalCode.text =  postIndexRecipient
            else:
                PostalCode.text = postIndexSender
                i = 0
                break
            i += 1
        for City in root.iter('City'):
            if not i:
                City.text =  whereCity
            else:
                City.text = fromCity
                i = 0
                break
            i += 1
        for CountryName in root.iter('CountryName'):
            if not i:
                CountryName.text =  whereCountry
            else:
                CountryName.text = fromCountry
                i = 0
                break
            i += 1
        for CountryCode in root.iter('CountryCode'):
            if not i:
                CountryCode.text =  whereCountryCode
            else:
                CountryCode.text = fromCountryCode
                i = 0
                break
            i += 1
        for Email in root.iter('Email'):
            Email.text = email
        for widthXML in root.iter('Width'):
            widthXML.text = width
        for Date in root.iter('Date'):
            Date.text = dateSend
        for PackageType in root.iter('PackageType'):
            PackageType.text = typeCode
        for Contents in root.iter('Contents'):
            Contents.text = type
        for GlobalProductCode in root.iter('GlobalProductCode'):
            GlobalProductCode.text = GlobalProductCodeType
        for LocalProductCode in root.iter('LocalProductCode'):
            LocalProductCode.text = GlobalProductCodeType
        for BillingAccountNumber in root.iter('BillingAccountNumber'):
            BillingAccountNumber.text = accountNumber
        for ShipperAccountNumber in root.iter('ShipperAccountNumber'):
            ShipperAccountNumber.text = accountNumber

        tree.write('static/files/req.xml', 'UTF-8')
        with open('static/files/req.xml') as inputfile:
            xml_file = inputfile.read()
        
        response = requests.post(
            'http://xmlpi-ea.dhl.com/XMLShippingServlet?isUTF8Support=true', data=xml_file)
        with open('static/files/resp.xml', 'w') as outfile:
            outfile.write(response.text)
        respRoot = ET.parse('static/files/resp.xml')

        for AirwayBillNumber in respRoot.iter('AirwayBillNumber'):
            trackcode = AirwayBillNumber.text

        Path('static/files/' + trackcode).mkdir(parents=True, exist_ok=True)

        for pdfXML in respRoot.iter('OutputImage'):
            with open('static/files/' + trackcode + '/Накладная.pdf', 'wb') as outpdf:
                outpdf.write(base64.b64decode(pdfXML.text))
        for pdfXML in respRoot.iter('DocImageVal'):
            with open('static/files/' + trackcode + '/Receipt.pdf', 'wb') as outpdf:
                outpdf.write(base64.b64decode(pdfXML.text))

        person = Order.objects.get(id=personID)
        person.apply = True
        person.trackcode = trackcode
        person.date = datetime.utcnow().strftime("%d.%m.%Y")
        person.save()
        msg = ''
        msg += 'Добрый день, Уважаемый Клиент!\n'
        msg += 'Выражаем благодарность за Ваш выбор. Ваша заявка успешно обработана и передана курьерам. В указанное время с Вами свяжутся и совершат забор посылки.Во вложении накладная по Вашему отправлению. Ее нужно будет распечатать и передать курьеру вместе с Вашей посылкой. \n'
        msg += 'Команда TATEX желает Вам удачных сделок и продуктивного дня!\n'
        msg += 'Ваш трек-код для отслеживания '
        msg += trackcode
        msg += '\n'
        msg += '*Не отвечайте на это письмо, оно автоматическое. Чтобы связаться с компанией TATEX, воспользуйтесь вариантами, представленными на нашем сайте tatex.kz'
        theme =  'Накладная по Вашему заказу'
        message = EmailMessage(
            theme,
            msg,
            to=[email]
        )
        filePath = 'static/files/' + trackcode + '/Накладная.pdf'
        message.attach_file(filePath)
        message.send()
        tree = ET.parse('static/files/callcourier.xml')
        root = tree.getroot()
        i = 0
        
        for MessageTime in root.iter('MessageTime'):
            MessageTime.text = datetime.utcnow().isoformat()
        for weightXML in root.iter('Weight'):
            weightXML.text = weight
        for PersonName in root.iter('PersonName'):
            if not i:
                PersonName.text = recipientName
            else:
                PersonName.text =  sendersName
                i = 0
                break
            i += 1
        for AddressLine1 in root.iter('Address1'):
            if not i:
                AddressLine1.text = recipientAddress
            else:
                AddressLine1.text =  sendersAddress
                i = 0
                break
            i += 1
        for PhoneNumber in root.iter('Phone'):
            if not i:
                PhoneNumber.text    =   recipientTel
            else:
                PhoneNumber.text    =   sendersTel
                i = 0
                break
            i += 1
        for PostalCode in root.iter('PostalCode'):
            PostalCode.text =  postIndexRecipient
        for City in root.iter('City'):
            if not i:
                City.text =  whereCity
            else:
                City.text = fromCity
                i = 0
                break
            i += 1
        for CountryCode in root.iter('CountryCode'):
            if not i:
                CountryCode.text =  whereCountryCode
            else:
                CountryCode.text = fromCountryCode
                i = 0
                break
            i += 1
        for StateCode in root.iter('StateCode'):
            StateCode.text = whereCountryCode
        for PickupDate in root.iter('PickupDate'):
            PickupDate.text = pickupDate[2] + '-' + pickupDate[1] + '-' + pickupDate[0]
        for AccountNumber in root.iter('AccountNumber'):
            AccountNumber.text = accountNumber
        for ReadyByTime in root.iter('ReadyByTime'):
            ReadyByTime.text = timeMin.split(':')[0] + ':' + timeMin.split(':')[1]
        for CloseTime in root.iter('CloseTime'):
            CloseTime.text = timeMax.split(':')[0] + ':' + timeMax.split(':')[1]
        tree.write('static/files/callcourier.xml', 'UTF-8')
        with open('static/files/callcourier.xml') as inputfile:
            xml_file = inputfile.read()
        
        response = requests.post(
            'http://xmlpi-ea.dhl.com/XMLShippingServlet?isUTF8Support=true', data=xml_file)
        print(response.text)
        respRoot = ET.fromstring(response.text)
        CourierNumber = ''
        for ConfirmationNumber in respRoot.iter('ConfirmationNumber'):
            CourierNumber = ConfirmationNumber.text
        person.courierNum = CourierNumber
        person.save()
        return JsonResponse({'Response': response.text})

    return JsonResponse({'dfd': 2})

@csrf_exempt
def status(request):
     if request.method == "POST":
        jsonReq = json.loads(request.body.decode('utf-8'))
        trackcode = jsonReq.get('trackcode', '')
        xml_file = '''
            <ns0:KnownTrackingRequest xmlns:ns0="http://www.dhl.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.dhl.com TrackingRequestKnown.xsd" schemaVersion="1.0">
                <Request>
                    <ServiceHeader>
                        <MessageTime>{0}</MessageTime>
                        <MessageReference>1234567890123456789012345678901</MessageReference>
                        <SiteID>v62_tBTTUgPMKT</SiteID>
                        <Password>y3vOe4xj9h</Password>
                    </ServiceHeader>
                </Request>
                <LanguageCode>RU</LanguageCode>
                <AWBNumber>{1}</AWBNumber>
                <LevelOfDetails>LAST_CHECK_POINT_ONLY</LevelOfDetails>
            </ns0:KnownTrackingRequest>
        '''.format(datetime.utcnow().isoformat(), str(trackcode))

        response = requests.post(
            'http://xmlpi-ea.dhl.com/XMLShippingServlet?isUTF8Support=true', data=xml_file)
       
        respRoot = ET.fromstring(response.text)
        events = []

        for ShipmentEvent in respRoot.iter('ShipmentEvent'):
            event = {}
            for Date in ShipmentEvent.iter('Date'):
                event['date'] = Date.text
            for Time in ShipmentEvent.iter('Time'):
                event['time'] = Time.text
            for ServiceEvent in ShipmentEvent.iter('ServiceEvent'):
                for Description in ServiceEvent.iter('Description'):
                    event['Status'] = Description.text.replace(
                        '<>', '')
                for EventCode in ServiceEvent.iter('EventCode'):
                    if EventCode.text == 'PU' or EventCode.text == 'FD' or EventCode.text == 'DF':
                        event['code'] = '_green-indicator'
                    elif EventCode.text == 'CS' or EventCode.text == 'OH' or EventCode.text == 'AF':
                        event['code'] = '_yellow-indicator'
                    elif EventCode.text == 'MS':
                        event['code'] = '_red-indicator'
                    else:
                        event['code'] = '_no-indicator'
            events.append(event)
       
        if(len(events) == 0):
            events.append('Полученные данные об отправлениях')
        try:
            person = Order.objects.get(trackcode=trackcode)
            person.status = events[0]
            person.save()
        except Order.DoesNotExist:
            return JsonResponse({'Status': "Error"})
        return JsonResponse({'Status': events})