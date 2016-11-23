from django.conf.urls import url, include
from printer import views

app_name = 'printer'

urlpatterns = [
    url(r'^printer/', include([
        url(r'^all/space/(\d+)/$', views.PrinterAllView.as_view(), name='printer_all'),
        url(r'^(\d+)/$', views.PrinterView.as_view(), name='printer'),
    ])),
    url(r'^cartridge/', include([
        url(r'^all/space/(\d+)/$', views.CartridgeAllView.as_view(), name='cartridge_all'),
        url(r'^(\d+)/$', views.CartridgeView.as_view(), name='cartridge'),
        url(r'^(\d+)/minus/$', views.CartridgeMinusView.as_view(), name='cartridge_minus'),
        url('^space/(\d+)/sendtorecycling/$', views.CartridgeSendToRecyclingView.as_view(),
            name='cartridge_send_to_recycling'),
        url('^space/(\d+)/inrecycling/$', views.CartridgeInRecyclingView.as_view(), name='cartridge_in_recycling'),
    ])),
    url(r'^zip/', include([
        url(r'^all/space/(\d+)/$', views.ZipAllView.as_view(), name='zip_all'),
        url(r'^(\d+)/$', views.ZipView.as_view(), name='zip'),
        url(r'^(\d+)/minus/$', views.ZipMinusView.as_view(), name='zip_minus'),
    ])),
]
