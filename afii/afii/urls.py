from django.conf.urls import url, include
from django.contrib import admin
from afii import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^space/', include('space.urls'), name='space'),
    url(r'^printer/', include('printer.urls'), name='printer'),
    url(r'^storage/', include('storage.urls'), name='storage'),
    url(r'^', include('inventory.urls'), name='inventory'),
]


# Django Debug Toolbar

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
