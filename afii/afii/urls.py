from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^space/', include('space.urls'), name='space'),
    url(r'^printer/', include('printer.urls'), name='printer'),
    #url(r'^', include(''), name=''),
    url(r'^', include('inventory.urls'), name='inventory'),
]
