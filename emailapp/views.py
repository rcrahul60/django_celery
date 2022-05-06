from django.http import HttpResponse
from django.shortcuts import render
from .tasks import sendMaill
# Create your views here.

def sendMail(request):
    sendMaill.delay()
    return HttpResponse('Mail Sent')