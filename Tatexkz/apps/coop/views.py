from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import EmailMessage

from Tatexkz.apps.coop.models import Coop, CoopSettings

# Create your views here.


def index(request):
    title = CoopSettings.objects.latest('title').title
    text = CoopSettings.objects.latest('text').text
    return render(
        request, 'coop/cooperation.html', {'title': title, 'text': text}
    )
def coopadd(request):
    if(request.POST):
        print(request.POST)
        geoStr = ''
        servicesStr = ''
        servicesStr = ', '.join(request.POST.getlist('services[]', ['Пользователь ничего не выбрал']))
        geoStr = ', '.join(request.POST.getlist('geo[]', ['Пользователь ничего не выбрал']))
        
        Coop (
            name = request.POST.get('name', ''),
            tel = request.POST.get('tel', ''),
            email = request.POST.get('email', ''),
            company = request.POST.get('company', ''),
            services = servicesStr,
            volume = request.POST.get('volume', ''),
            cargo = request.POST.get('cargo', ''),
            geo = geoStr
        ).save()


        msg = ''
        msg += 'ФИО: ' + request.POST.get('name', '') + '\n'
        msg += 'Контактный телефон: ' + request.POST.get('tel', '') + '\n'
        msg += 'E-Mail: ' + request.POST.get('email', '') + '\n'
        msg += 'Название компании: ' + request.POST.get('company', '') + '\n'
        msg += 'Услуги: ' + servicesStr + '\n'
        msg += 'Ожидаемый объем отправлений (шт в месяц): ' + request.POST.get('volume', '') + '\n'
        msg += 'Характер груза: ' + request.POST.get('cargo', '') + '\n'
        msg += 'География отправок: ' + geoStr + '\n'

        message = EmailMessage(
            'Создана новая заявка на сотрудничество Tatex.kz',
            msg,
            to=['info@tatex.kz']
        )
        message.send(fail_silently=True)
    return HttpResponseRedirect("/coop/#popup_success_coop")
