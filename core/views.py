from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

##WELCOME VIEW
def index(request):
    return render(request,"core/index.html")