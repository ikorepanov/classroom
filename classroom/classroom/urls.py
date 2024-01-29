from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('seats.urls', namespace='seats')),
    path('admin/', admin.site.urls),
]
