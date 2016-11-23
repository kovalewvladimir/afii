from django.conf.urls import url, include
from element import views


app_name = 'element'

urlpatterns = [
    url(r'^paper/', include([
        url(r'^space/(\d+)/$', views.PaperAllView.as_view(), name='paper_all'),
        url(r'^(\d+)/$', views.PaperView.as_view(), name='paper'),
        url(r'^(\d+)/minus/$', views.PaperMinusView.as_view(), name='paper_minus'),
    ])),
    url(r'^distribution/', include([
        url(r'^space/(\d+)/$', views.DistributionAllView.as_view(), name='distribution_all'),
        url(r'^(\d+)/$', views.DistributionView.as_view(), name='distribution'),
    ])),
    url(r'^computer/', include([
        url(r'^space/(\d+)/$', views.ComputerAllView.as_view(), name='computer_all'),
        url(r'^(\d+)/$', views.ComputerView.as_view(), name='computer'),
    ])),
]
