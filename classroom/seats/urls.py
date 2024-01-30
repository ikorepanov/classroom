from django.urls import path

from . import views

app_name = 'seats'

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('success', views.success, name='success'),
]
