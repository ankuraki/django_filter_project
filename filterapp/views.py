

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from filterapp.forms import UserRegisterForm,UserLoginForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import  login_required
from filterapp.filter import UserFilter

# Create your views here.

def home(request):
    return render(request,'home.html')


def register_view(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=request.POST.get('username','')
            first_name=request.POST.get('first_name','')
            last_name=request.POST.get('last_name','')
            password1=request.POST.get('password1','')
            password2=request.POST.get('password2','')
            email=request.POST.get('email','')

            if User.objects.filter(username=username,email=email).exists():
                messages.warning(request, f"Your username/email already taken")
                return redirect('register')


            if password1 != password2:
                messages.warning(request, f"Your password and Confirm password should be same.")
                return redirect('register')

            User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password1,
                email=email,
            )
            messages.success(request, f"Your Registration Done Successfully.")
            return redirect('login')
            
        else:
            context={
                "error":"form is not valid please check again.."
            }
            return render(request,'register.html',context)
    else:
        form=UserRegisterForm()
        context={
            'form':form,
            'error':"form object not created.."
        }
        return render(request,'register.html',context)


def login_view(request):
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=request.POST.get('username','')
            password=request.POST.get('password','')

            user = authenticate(username=username,password=password)

            if user is None:
                messages.warning(request, f'Invalid username/password')
                return redirect('login')
            else:
                login(request,user)
                messages.success(request, f'Your Login Successfully..')
                return redirect('search')
        else:
            context={
                'error':'form is not valid , please check again.'

            }
            return render(request,'login.html',context)

    else:
        form=UserLoginForm()
        context={
            'form':form ,
            'error':'form object not created.'
        }
        return render(request,'login.html',context)

     

# def logout_view(request):
#     user = request.user
#     logout(user)
#     messages.success(request, f'You are logged out now successfully')
#     return redirect('login')

def logout_view(request):
    logout(request)
    messages.success(request,f"You are loggout successfully.")
    return redirect("login")


def search_view(request):
    user_list=User.objects.all()
    user_filter=UserFilter(request.GET, queryset=user_list)
    context={
        'filter':user_filter
    }
    return render(request,'user_list.html',context)
