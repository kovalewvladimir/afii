from django.conf.urls import url
from printer import views

app_name = 'printer'

urlpatterns = [
    url(r'^all/space/(\d+)/$', views.PrinterAllView.as_view(), name='printer_all'),
    url(r'^cartridge/all/space/(\d+)/$', views.CartridgeAllView.as_view(), name='cartridge_all'),
    url(r'^zip/all/space/(\d+)/$', views.ZipAllView.as_view(), name='zip_all'),

    url(r'^(\d+)/$', views.PrinterView.as_view(), name='printer'),
    url(r'^cartridge/(\d+)/$', views.CartridgeView.as_view(), name='cartridge'),
    url(r'^zip/(\d+)/$', views.ZipView.as_view(), name='zip'),

    url(r'^cartridge/(\d+)/minus/$', views.CartridgeMinusView.as_view(), name='cartridge_minus'),
    url(r'^zip/(\d+)/minus/$', views.ZipMinusView.as_view(), name='zip_minus'),
]
