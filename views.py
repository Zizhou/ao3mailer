from django.shortcuts import render
from django.http import HttpResponse

from ao3mailer import mailbot, mail_test

import sys

# Create your views here.



def main_page(request):
    return HttpResponse("There is nothing here. Go away.")

def mailer(request):
    mail = request.GET.get('mail')
    url = request.GET.get('url')


    print >>sys.stderr, url
    urlplus = url# + "?view_adult=true" #so lazy
    info = "Mail: " + mail + " URL: " + urlplus
    #mailbot.send_mail(mailbot.diagnostic(info, mail), mail) 
    message = mailbot.pack_MIME(mail, urlplus)
    if message:
        mailbot.send_mail(message, mail)
        print "it worked?"
    else:
        return HttpResponse('well, you done fucked up, but you already knew that')
    return HttpResponse(info)

def test_mailer(request):
    #mail_test.run_diagnostic()
    #mail_test.run_test()
    mail = request.GET.get('mail')
    url = request.GET.get('url')


    return_string = mail + ' ' + url
    return HttpResponse(return_string)
