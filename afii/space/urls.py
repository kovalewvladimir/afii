from django.conf.urls import url
from space import views

app_name = 'space'

urlpatterns = [
    url(r'^(\d+)/', views.space_view, name='space'),
]
