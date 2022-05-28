"""Tatexkz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('admin/', admin.site.urls),
] + i18n_patterns(
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('Tatexkz.apps.home.urls')),
    path('tracking/', views.tracking, name="tracking"),
    path('oferta/', views.oferta, name="oferta"),
    path('privacy/', views.privacy, name="privacy"),
    path('gotodhl/', views.dhl, name="dhl"),
    path('payment/', include('Tatexkz.apps.payment.urls')),
    path('coop/', include('Tatexkz.apps.coop.urls')),
    path('order/', include('Tatexkz.apps.order.urls')),
    path('promo/', include('Tatexkz.apps.promo.urls')),
    prefix_default_language=False,
)