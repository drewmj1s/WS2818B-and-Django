"""blinkled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    #url(r'^on/(?P<pattern_color>#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})+)/(?P<pattern_speed>[1-5]{1})/(?P<pattern_leds>[1-9]{3})/(?P<pattern_baf>+)$', views.on_page, name='on_page'),
    #url(r'^on/(<?Ppattern_color>#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})+)/(?P<pattern_speed>[1-5]{1})/<pattern_leds>/<pattern_baf>$', views.on_page, name='on_page'),
    #url(r'^on/(?P<pattern_color>#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})+)$', views.on_page, name='on_page'),
    #url('on/<slug:pattern_color>/<int:pattern_speed>', views.on_page, name='on_page'),
    #url(r'^on/(?P<pattern_color>#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})+)/(?P<pattern_speed>[1-5]{1})/<pattern_baf>$', views.on_page, name='on_page'),
    #url(r'^(?P<pattern_speed>[1-5]{1})/(?P<pattern_color>#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})+)/(?P<pattern_name>/w+)$', views.on_page, name='on_page'),
    url(r'^(?P<pattern_name>.+?)/(?P<pattern_speed>[1-5]{1})/(?P<pattern_color>#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})+)/(?P<pattern_baf>.+?)/(?P<pattern_leds>.+?)$', views.on_page, name='on_page'),
    url('off/', views.turnOff, name='off_page'),
]

