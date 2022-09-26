""" Views file for menu app """
from django.views.generic import DetailView, ListView
from .models import Menu


class AllMenusView(ListView):
    """ list view for all available menus """
    model = Menu
    template_name = 'menu/menu.html'
    context_object_name = 'menu'
    queryset = Menu.objects.all().order_by('menu_name')


class IndividualMenuDetail(DetailView):
    """ Single Menu view to allow users to view the
        individual menu chosen in more detail"""
    model = Menu
