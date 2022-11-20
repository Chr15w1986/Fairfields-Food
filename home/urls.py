""" Home app url config file """
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.aboutus, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('bookus', views.bookus, name='book-us'),
]
