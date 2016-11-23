from django.conf.urls import url
from django.views.generic import RedirectView

from inventory import views

app_name = 'inventory'

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/printer/printer/all/space/1/'), name='main'),
]
