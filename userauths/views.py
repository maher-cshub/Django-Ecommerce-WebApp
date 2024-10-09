from django.shortcuts import render,redirect
from userauths.forms import UserRegisterForm,UserLoginForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def register_view(request):
    ##CHECK IF USER IS AUTHENTICATED
    if request.user.is_authenticated:
        return redirect("core:index")

    ##CHECK IF THE METHOD IS POST
    if request.method == "POST":

        ##GRAB THE FORM DATA FROM FRONTEND AND BUILD THE FORM MODEL
        form = UserRegisterForm(request.POST or None)

        ##CHECK IF THE FORM IS VALID
        if form.is_valid():

            ##CREATE THE USER IN DB
            new_user = form.save()
            username = form.cleaned_data.get("email")

            ##LOGIN THE USER
            new_user = authenticate(username = username, password = form.cleaned_data.get("password1"))
            login(request,new_user)
                
            ##SUCCESS MESSAGE
            messages.success(request,f"Welcome {new_user.username}!")

            #SAVE USER INFO IN SESSION
            request.session['user'] = {"username":new_user.username,"email":new_user.email}

            ##REDIRECT TO HOME
            return redirect("core:index")
        else:
            messages.error(request,f'{form.errors}')   
            return   

    else:
        ##BUILD THE FORM MODEL
        form = UserRegisterForm()

        context = {"register_form":form}

        return render(request,"userauths/register.html",context=context)



def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect("core:index")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("userauths:login")
            
    else:
        form = UserLoginForm()
        context = {"login_form": form}
        return render(request,"userauths/login.html",context=context)


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect("core:index")
    logout(request)
    return redirect("userauths:login")
