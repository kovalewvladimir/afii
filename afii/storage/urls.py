from django.conf.urls import url
from storage import views

app_name = 'storage'

urlpatterns = [
    url(r'^(\d+)/$', views.StorageView.as_view(), name='storage_all'),
    url(r'^itemstorage/(\d+)/$', views.ItemStorageView.as_view(), name='itemstorage'),
]
