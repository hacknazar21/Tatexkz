import base64
from datetime import datetime
import json
from re import sub
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as BS
import xml.etree.ElementTree as ET
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from Tatexkz.apps.payment.models import Order
from transliterate import translit
from pathlib import Path
import xml.dom.minidom

countiesRoot = ET.parse('static/files/counties-codes.xml')
countriesCodes = {}
for country in countiesRoot.iter('country'):
    for name in country.iter('name'):
        for alpha2 in country.iter('alpha2'):
            countriesCodes[name.text] = alpha2.text


def home(request):
    return render(
        request, 'home/index.html'
    )


def tracking(request):
    if(request.GET):
        try:
            trackcode = request.GET.get('trackcode', '')
            try:
                person = Order.objects.get(trackcode=trackcode)
            except Order.DoesNotExist:
                return HttpResponse("Ой. Что-то пошло не так. Возможно, данного трек-кода не существует")

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
            print(response.text)
            for ShipmentDate in respRoot.iter('ShipmentDate'):
                dateShipment = datetime.fromisoformat(
                    ShipmentDate.text).strftime("%d.%m.%Y")
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
            return HttpResponse("Ой. Что-то пошло не так. Возможно, данного трек-кода не существует")

    return render(
        request, 'tracking/tracking.html', {
            'trackcode': trackcode,
            'dateShipment': dateShipment,
            'addressStr': addressStr,
            'dateApply': dateApply,
            'events': events
        }
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

        dateSend = datetime.strptime(jsonReq.get(
            'dateSend', ''), '%d/%m/%Y').strftime("%Y-%m-%d")

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
        if whereCountry == fromCountry:
            GlobalProductCodeType = 'N'
            accountNumber = '376165440'
        elif jsonReq.get('whereCountry', '') == 'Казахстан':
            accountNumber = '967710648'
        elif jsonReq.get('fromCountry', '') == 'Казахстан':
            accountNumber = '376165440'
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
                PersonName.text = sendersName
                i = 0
                break
            i += 1
        for AddressLine1 in root.iter('AddressLine1'):
            if not i:
                AddressLine1.text = recipientAddress
            else:
                AddressLine1.text = sendersAddress
                i = 0
                break
            i += 1
        for PhoneNumber in root.iter('PhoneNumber'):
            if not i:
                PhoneNumber.text = sendersTel
            else:
                PhoneNumber.text = recipientTel
                i = 0
                break
            i += 1
        for PostalCode in root.iter('PostalCode'):
            if not i:
                PostalCode.text = postIndexRecipient
            else:
                PostalCode.text = postIndexSender
                i = 0
                break
            i += 1
        for City in root.iter('City'):
            if not i:
                City.text = whereCity
            else:
                City.text = fromCity
                i = 0
                break
            i += 1
        for CountryName in root.iter('CountryName'):
            if not i:
                CountryName.text = whereCountry
            else:
                CountryName.text = fromCountry
                i = 0
                break
            i += 1
        for CountryCode in root.iter('CountryCode'):
            if not i:
                CountryCode.text = whereCountryCode
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
            with open('static/files/' + trackcode + '/Details.pdf', 'wb') as outpdf:
                outpdf.write(base64.b64decode(pdfXML.text))
        for pdfXML in respRoot.iter('DocImageVal'):
            with open('static/files/' + trackcode + '/Receipt.pdf', 'wb') as outpdf:
                outpdf.write(base64.b64decode(pdfXML.text))

        person = Order.objects.get(id=personID)
        person.apply = True
        person.trackcode = trackcode
        person.date = datetime.utcnow().strftime("%d.%m.%Y")
        person.save()

        return JsonResponse({'Response': response.text})

    return JsonResponse({'dfd': 2})
