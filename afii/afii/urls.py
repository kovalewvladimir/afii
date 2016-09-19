from django.conf.urls import url, include
from django.contrib import admin
from afii import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('inventory.urls')),
]

# django debug toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]