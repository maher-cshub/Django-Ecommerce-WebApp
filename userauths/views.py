from django.shortcuts import render
from userauths.forms import UserRegisterForm
# Create your views here.

def register_view(request):
    form = UserRegisterForm()
    #context
    context = {
        "register_form":form
    }
    return render(request,"userauths/register.html",context=context)




