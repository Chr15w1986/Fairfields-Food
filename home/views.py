""" Home, about, gallery page views """

from django.shortcuts import render


def index(request):
    """ View to return the home/landing page """
    return render(request, 'home/index.html')


def aboutus(request):
    """ View to return the about us page """
    return render(request, 'home/about.html')


def gallery(request):
    """ View to return the gallery page """
    return render(request, 'home/gallery.html')


def bookus(request):
    """ View to return the book us/contact page """
    return render(request, 'home/bookus.html')
