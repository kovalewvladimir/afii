from django.conf.urls import url
from element import views
from django.views.generic import ListView


app_name = 'element'

urlpatterns = [
    url(r'^paper/space/(\d+)/$', views.PaperAllView.as_view(), name='paper_all'),
    url(r'^distribution/space/(\d+)/$', views.DistributionAllView.as_view(), name='distribution_all'),
    url(r'^computer/space/(\d+)/$', views.ComputerAllView.as_view(), name='computer_all'),
    url(r'^paper/(\d+)/$', views.PaperView.as_view(), name='paper'),
    url(r'^distribution/(\d+)/$', views.DistributionView.as_view(), name='distribution'),
    url(r'^computer/(\d+)/$', views.ComputerView.as_view(), name='computer'),
]
