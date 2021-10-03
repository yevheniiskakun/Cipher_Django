from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from cipher import settings
from pages import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='home'),
]
