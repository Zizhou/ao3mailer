import mailbot

def run_test():
    mobi_file = mailbot.get_file('http://archiveofourown.org/works/829218?view_adult=true')

    print mobi_file
    print "now testing MIME packing"
    mime = mailbot.pack_MIME('givemeviruses@gmail.com', 'http://archiveofourown.org/works/829218?view_adult=true')

    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print 'now sending...'
    mailbot.send_mail(mime, 'givemeviruses@gmail.com')
    print 'done!'

def run_diagnostic():
    mail = mailbot.diagnostic('I am the very model of a modern major general','givemeviruses@gmail.com')

    mailbot.send_mail(mail, 'givemeviruses@gmail.com')
