from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from videochatting.models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
     
    return render(request ,'base.html')
   
    #return HttpResponse("This is home page")

def about(request):
    return render(request, 'aboutus.html')

def newmeeting(request):
    return render(request, 'newmeeting.html')
def logout(request):
    return render(request, 'signin.html')
def leavemeeting(request):
    return render(request, 'contact.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        feedback = request.POST.get('feedback')
        contact=Contact(name=name,email=email,phone=phone ,feedback=feedback,date=datetime.today() )
        contact.save()
        
    return render(request, 'contact.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        #username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if len(username) >15:
            messages.error(request, "Username must be less than 15 characters")
            return redirect('/signup')
        
        if not  username.isalnum():
            messages.error(request, "Username must be alphanumeric")
            return redirect('/signup')
        
        if password1!= password2:
            messages.error(request, "Password must be equal to password1 and password2") 
            return redirect('/ Signup')
        
        
        
        myuser= User.objects.create_user(username,email,password1)
        myuser.save()
        messages.success(request,"Your account has been created successfully")
        return redirect('/signin')
     
    return render(request,'register.html')
def signin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username =loginusername, password=loginpassword)
        
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('/signin')
       
        
        
    return render(request, 'signin.html')