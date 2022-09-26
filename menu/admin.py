""" Admin file for menu app """
from django.contrib import admin
from .models import Menu, OrderHistory

admin.site.register(Menu)
admin.site.register(OrderHistory)
