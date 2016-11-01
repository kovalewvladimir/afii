from django.conf.urls import url
from element import views


app_name = 'element'

urlpatterns = [
    url(r'^paper/(\d+)/$', views.paper_view, name='paper'),
    url(r'^distribution/(\d+)/$', views.distribution_view, name='distribution'),
    url(r'^computer/(\d+)/$', views.computer_view, name='computer'),
]
