import mailbot

###REPLACE THIS!!
mail_to = 'mail@mail.mail'
###

def run_test():
    mobi_file = mailbot.get_file('http://archiveofourown.org/works/829218?view_adult=true')

    print mobi_file
    print "now testing MIME packing"
    mime = mailbot.pack_MIME(mail_to, 'http://archiveofourown.org/works/829218?view_adult=true')

    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print 'now sending...'
    mailbot.send_mail(mime, mail_to)
    print 'done!'

def run_diagnostic():
    mail = mailbot.diagnostic('I am the very model of a modern major general',mail_to)

    mailbot.send_mail(mail, mail_to)
