from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import User
from django.forms import forms

class RegisterForm(forms.Form):
    

# Create your views here.
def index(request):
    return render(request, "oneWorldApp/index.html", {
    })

def register(request):
    pass