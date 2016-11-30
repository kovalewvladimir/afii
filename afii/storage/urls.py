from django.conf.urls import url
from storage import views

app_name = 'storage'

urlpatterns = [
    url(r'^(\d+)/$', views.StorageView.as_view(), name='storage_all'),
    url(r'^(\d+)/add_category$', views.AddCategoryView.as_view(), name='add_category'),
    url(r'^itemstorage/(\d+)/$', views.ItemStorageView.as_view(), name='itemstorage'),
    url(r'^itemstorage/(\d+)/minus/$', views.ItemStorageMinusView.as_view(), name='itemstorage_minus'),
]
