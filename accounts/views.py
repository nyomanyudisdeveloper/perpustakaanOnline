from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, logout, get_user_model, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def login_process(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user_model = get_user_model()
        user = user_model.objects.filter(email=email).first()
        if user is not None:
            username = user.username
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/pinjamBuku/")
            else:
                return render(request,'login.html',{'error':'Email or password is incorrect','email':email,'password':password})
        else:
            return render(request,'login.html',{'error':'Email or password is incorrect','email':email,'password':password})
    else:
        if request.user.is_authenticated:
            return redirect("/pinjamBuku/")
        return render(request,"login.html");

def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        error_email_list = []
        user_model = get_user_model()
        user = user_model.objects.filter(email=email).first()
        if user is not None:
            error_email_list.append("email is already exists")

        error_password_list = []
        if len(password) != 8:
            error_password_list.append("password must have 8 length character")
        if not password.isalnum():
            error_password_list.append("password can't contain special character")
        
        is_contain_one_upper_char = False
        for char in password:
            if char.isupper():
                is_contain_one_upper_char = True
                break
        
        if is_contain_one_upper_char == False:
            error_password_list.append("password must contain one uppercase character")

        error_cpassword_list = []
        if password != cpassword:
            error_cpassword_list.append("password and confirm password must be same")
        
        if len(error_email_list) > 0 or len(error_password_list) > 0 or len(error_cpassword_list) > 0:
            return render(request,"register.html",{
                'firstName':firstName,
                'lastName':lastName,
                'username':username,
                'email':email,
                'password':password,
                'cpassword':cpassword,
                'error_password_list':error_password_list,
                'error_cpassword_list':error_cpassword_list, 
                'error_email_list':error_email_list
            })
        else:
            user = User.objects.create_user(username, email, password)
            user.first_name = firstName
            user.last_name = lastName
            user.save()

            user = authenticate(request,username=username,password=password)
            login(request,user)
            return redirect("/pinjamBuku/")
    if request.user.is_authenticated:
        return redirect("/pinjamBuku/")
    return render(request,"register.html");


def logout_process(request):
    logout(request)
    return redirect("/accounts/login/")
    