from django.conf.urls import url, include
from inventory import views

app_name = 'inventory'
urlpatterns = [
    url(r'^space/(?P<space_id>\d+)/', include([
        url(r'^$', views.printers, name='space'),
        url(r'^printers/$', views.printers, name='printers'),
        url(r'^cartridges/$', views.cartridges, name='cartridges'),
        url(r'^zips/$', views.zips, name='zips'),
        url(r'^papers/$', views.papers, name='papers'),
        url(r'^distributions/$', views.distributions, name='distributions'),
        url(r'^computers/$', views.computers, name='computers'),
        #url(r'^/$', views., name=''),
    ])),

    url(r'^printer/(\d+)/$', views.printer, name='printer'),
    url(r'^cartridge/(\d+)/', views.cartridge, name='cartridge'),
    url(r'^zip/(\d+)/', views.zip, name='zip'),
    url(r'^paper/(\d+)/', views.paper, name='paper'),
    url(r'^distribution/(\d+)/', views.distribution, name='distribution'),
    url(r'^computer/(\d+)/', views.computer, name='computer'),
    #url(r'^', views., name=''),

    url(r't/$', views.main),
]
