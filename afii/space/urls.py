from django.conf.urls import url
from django.views.generic import RedirectView

app_name = 'space'

urlpatterns = [
    url(r'^(\d+)/$', RedirectView.as_view(pattern_name='printer:printer_all'), name='space'),
]
