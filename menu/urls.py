""" Menu app url config file """
from django.urls import path
from .views import AllMenusView

APP_NAME = 'menu'
urlpatterns = [
    path('', AllMenusView.as_view(), name='menu'),
]
