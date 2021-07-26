from django.urls import path
from rango import views
from rango import about

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('', about.index2, name='index2'),
]
