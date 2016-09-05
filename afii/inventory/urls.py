from django.conf.urls import url
from inventory import views

app_name = 'inventory'
urlpatterns = [
    url(r'$', views.main, name='main'),
]
