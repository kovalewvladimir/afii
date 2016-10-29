from django.conf.urls import url
from storage import views

app_name = 'storage'

urlpatterns = [
    url(r'(\d+)/$', views.storage_view, name='storage_all')
]
