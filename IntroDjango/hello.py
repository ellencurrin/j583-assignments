#!/usr/bin/env python

import sys
 
from django.conf import settings
from django.conf.urls import patterns
from django.http import HttpResponse
from django.core.management import execute_from_command_line
 
settings.configure(
    #set debug to FALSE when the page is live
    DEBUG=True,
    #secret key is necessary for security
    SECRET_KEY='placerandomsecretkeyhere',
    ROOT_URLCONF=sys.modules[__name__],
)
 
def index(request):
    return HttpResponse('Powered by Django')
 
#configures url
urlpatterns = patterns('', 
    #(regex (regular expression), function="index") 
    (r'^$', index),
)
 
if __name__ == "__main__":
    execute_from_command_line(sys.argv)

