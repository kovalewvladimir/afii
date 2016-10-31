from django.conf.urls import url
from element import views


app_name = 'element'

urlpatterns = [
    url(r'^paper/(\d+)/$', views.paper_view, name='paper'),
]
