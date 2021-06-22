import re
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request,'index.html')

# localhost:8000/user/create_user

def create_user(request):
    if request.method == "POST":
        # validacion check before safa in our DB
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/')

        hash_pw = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode()
        print(hash_pw)
        new_user = User.objects.create(
            name = request.POST['name'],
            alias = request.POST['alias'],
            email = request.POST['email'],
            password = hash_pw
        )
        request.session['logged_user'] = new_user.id

        return redirect('/user/dashboard')
    return redirect("/")
    # local

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email = request.POST['email'])
        if user:
            log_user = user [0]
            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                request.session['logged_user'] = log_user.id
                return redirect('/user/dashboard')
        messages.error(request, "Email/password are incorect. Please Retry")
    return redirect("/")

def logout(request):
    request.session.flush()
    return redirect('/')
    

# def dashboard(request):
# def create_book(request):
# def Book_form(request):
# def show_book(request,book_id):
# def add_review(request):
# def user_page(request,user_id):
# def delete_review(request,review_id):


