from django.conf.urls import url
from printer import views

app_name = 'printer'

urlpatterns = [
    url(r'^all/space/(\d+)/$', views.printer_all_view, name='printer_all'),
    url(r'^cartridge/all/space/(\d+)/$', views.cartridge_all_view, name='cartridge_all'),
    url(r'^zip/all/space/(\d+)/$', views.zip_all_view, name='zip_all'),
]
