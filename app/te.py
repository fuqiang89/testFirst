# -*- coding: cp936 -*-
__author__ = 'tongbuop'

from django.template.loader import get_template
from django.template import Context
from django.http import *
import datetime
def current_datetime(request):
    #now = datetime.datetime.now()
    now = request.GET
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

print "test git"












