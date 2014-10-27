from django.shortcuts import render
from django.http import HttpResponse

from ao3mailer import mailbot

# Create your views here.



def main_page(request):
    return HttpResponse("There is nothing here. Go away.")

def mailer(request, mail, url):
    urlplus = url + "?view_adult=true" #so lazy
    info = "Mail: " + unicode(mail) + " URL: " + unicode(urlplus)

    message = mailbot.pack_MIME(mail, urlplus)
    if message:
        mailbot.send_mail(message, mail)
        print "it worked?"
    return HttpResponse(info)
