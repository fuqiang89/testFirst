# -*- coding: cp936 -*-
__author__ = 'tongbuop'

from django.template.loader import get_template
from django.template import Context
from django.http import *
import datetime
from models import snmpwalk_e
def current_datetime(request):
    #now = datetime.datetime.now()
    now = request.GET
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def real_time(request):
    tm = datetime.datetime.now()
    t = get_template('jsget.html')
    test_h = t.render(Context({'test_data': tm}))
    
    return HttpResponse(test_h)

def js_get(request):
#    jt = datetime.datetime.now()
    jt = snmpwalk_e(oid='1.3.6.1.2.1.25.3.3.1.2')
    return HttpResponse(jt)
    
def realtime(request):
    tm = datetime.datetime.now()
    t = get_template('realtime.html')
    html_t = t.render(Context({'test_data': tm}))
    return HttpResponse(html_t)



