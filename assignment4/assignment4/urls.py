from django.contrib import admin
from django.urls import path
from calculator.views import calculate_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', calculate_view, name='calculate'),
]