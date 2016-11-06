from django.conf.urls import url
from printer import views

app_name = 'printer'

urlpatterns = [
    url(r'^all/space/(\d+)/$', views.printer_all_view, name='printer_all'),
    url(r'^cartridge/all/space/(\d+)/$', views.cartridge_all_view, name='cartridge_all'),
    url(r'^zip/all/space/(\d+)/$', views.zip_all_view, name='zip_all'),
    url(r'^(\d+)/$', views.PrinterView.as_view(), name='printer'),
    url(r'^cartridge/(\d+)/$', views.CartridgeView.as_view(), name='cartridge'),
    url(r'^zip/(\d+)/$', views.ZipView.as_view(), name='zip'),
]
