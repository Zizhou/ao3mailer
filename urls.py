from django.conf.urls import patterns, url

from ao3mailer import views

urlpatterns = patterns('',
    url(r'^$', views.main_page, name = 'main'),
    #FUCKING regex
    url(r'^mailer/mail=(?P<mail>.*)&url=(?P<url>.*)$', views.mailer, name = 'mailer'), 
)
