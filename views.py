
from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    return render(request,'registration.html')# render have three argument one is necessary request and you put one for run server some any html file and third is filez
# def capital(request):
#     return HttpResponse("<h2>capital</h2> <a href='/'>back</a>")
def login(request):
    return render(request,'login.html')
