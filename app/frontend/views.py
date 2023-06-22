from django.shortcuts import render
from icecream import ic


# Create your views here.


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        ic(request.POST.get("name"))
        ic(request.POST.get("phone"))
        ic(request.POST.get("message"))
    return render(request, "contacts.html")
