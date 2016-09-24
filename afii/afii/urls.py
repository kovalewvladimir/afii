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

# Раздача media
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
