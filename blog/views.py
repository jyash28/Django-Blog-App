from django.shortcuts import render

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
    pass

# Signup
def signup(request):
    return render(request,'blog/signup.html')

# Login
def user_login(request):
    return render(request,'blog/login.html')

