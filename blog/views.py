from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm

# home
def home(request):
    return render(request,'blog/home.html')

# about
def about(request):
    return render(request,'blog/about.html')

# contact
def contact(request):
    return render(request,'blog/contact.html')

# dashboard         
def dashboard(request):
    return render(request,'blog/dashboard.html')

# Logout
def user_logout(request):
    return HttpResponseRedirect('/')

# Signup
def user_signup(request):
    form = SignUpForm()
    return render(request,'blog/signup.html',{'form':form})

# Login
def user_login(request):
    return render(request,'blog/login.html')

