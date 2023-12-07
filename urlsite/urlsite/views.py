from django.http import HttpResponse
from django.shortcuts import render

MENU = {"HOME": "/", "About": "/about", "Reviews": "/form"}
CHARACTER = {"Leon Kennedy": "/leon", "Jill Valentine": "/jill", "Chris Redfield": "/chris"}
def main_page(request):
    title = "RESIDENT EVIL"
    data = {"menu": MENU, "character": CHARACTER, "title": title}
    return render(request, "./index.html", context=data)

def leon_page(request):
    title = "Leon Scott Kennedy"
    data = {"menu":MENU}
    return render(request, "./leon.html", context=data)

def jill_page(request):
    title = "Jill Valentine"
    data = {"menu":MENU}
    return render(request, "./jill.html", context=data)

def chris_page(request):
    title = "Chris Redfield"
    data = {"menu":MENU}
    return render(request, "./chris.html", context=data)

def about_page(request):
    title = "BLOG"
    data = {"menu":MENU, "title": title}
    return render(request, "./about.html", context=data)


