from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    """ Menu options """
    menu_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    price_id = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.menu_name


class OrderHistory(models.Model):
    """ User order history within the user profile """
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    order_date = models.DateField(auto_now=False, blank=False, default=None)
    menu_type = models.ForeignKey('Menu', on_delete=models.CASCADE)
