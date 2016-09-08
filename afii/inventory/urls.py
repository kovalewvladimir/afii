from django.conf.urls import url
from inventory import views

app_name = 'inventory'
urlpatterns = [
    url(r't/$', views.main, name='main'),
]
