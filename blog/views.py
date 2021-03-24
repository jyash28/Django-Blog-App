from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post

# home
def home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

# about
def about(request):
    return render(request,'blog/about.html')

# contact
def contact(request):
    return render(request,'blog/contact.html')

# dashboard         
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request,'blog/dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect("/login/")

    

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Signup
def user_signup(request):
    if request.method == "POST":
        form= SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulation !! You have become an Author")
            form.save()
    else:
        form = SignUpForm()
    return render(request,'blog/signup.html',{'form':form})                             
    

# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data["username"]
                upass=form.cleaned_data["password"]
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged in successfully!!!")
                    return HttpResponseRedirect("/dashboard/")
        else:
            form =LoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect("/dashboard/")
    
