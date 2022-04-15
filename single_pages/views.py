<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )


def landing(request):
    return render(
        request,
        'single_pages/landing.html'
=======
from django.shortcuts import render

# Create your views here.
def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )


def landing(request):
    return render(
        request,
        'single_pages/landing.html'
>>>>>>> 2b873285fa3dcb81adb3d0df8df345db7fc979d7
    )