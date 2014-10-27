import re, email, time, urllib, smtplib

from email.mime.multipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.mime.text import MIMEText
from email import Encoders

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'devletter.settings'

from django.conf import settings

import sys

def pack_MIME(send_to, file_url):
    try:
        attachment = get_file(file_url)
    except Exception as e:
        print >> sys.stderr, e
        return False
    mail = MIMEMultipart('alternative')
    mail['Subject'] = "Automated .mobi mailing."
    mail['From'] = settings.AO3_MAILER 
    mail['To'] = send_to
    message = "Automated .mobi file mailing."
    body = MIMEText(message, 'html', 'UTF-8')
    mail.attach(body)

    try:
        attach_mobi = MIMEBase('application', "octet-stream")
        attach_mobi.set_payload(open(attachment, "rb").read())
        Encoders.encode_base64(attach_mobi)
        mobi_header = 'attachment; filename='+str(clean_name(attachment))
        attach_mobi.add_header('Content-Disposition', mobi_header)
        mail.attach(attach_mobi)
    except Exception as e:
        print >> sys.stderr, e
        return False

    return mail

def send_mail(mail, address):
    print mail
    #probably should be a setting and not hardcoded, but eh
    server = smtplib.SMTP('smtp.gmail.com','587')
    server.ehlo()
    server.starttls() 
    server.login(settings.AO3_MAILER, settings.AO3_PASSWORD)
    server.sendmail(settings.AO3_MAILER, address, mail.as_string())
    server.quit()

def get_file(url):
    page = urllib.urlopen(url)
    file_url = 'http://archiveofourown.org'

    for line in page.readlines():
        mobi_re = re.match(r'(.*)(href=")(?P<mobi>.*)(">MOBI)(.*)', line)
        if mobi_re:
            file_url += mobi_re.group('mobi')
    print 'the file is at...'
    print  file_url
    try:
        mobi_file = urllib.urlretrieve(file_url)
    except Exception as e:
        print >> sys.stderr, e
        return False
    print mobi_file
    return mobi_file[0]

def clean_name(name):
    mobi_re = re.match(r'(.*/)(?P<mobi>.*)(\.mobi)', name)
    return mobi_re.group('mobi') + '.mobi'
