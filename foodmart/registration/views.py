from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # return HttpResponse('Home Page')
    return render(request, 'registration/home.html')
def contact(request):
    # return HttpResponse('Contact Page')
    return render(request,'registration/contact.html')
def signup(request):
    # return HttpResponse('Sign Up')
    return render(request,'registration/signup.html')
def signin(request):
    # return HttpResponse('Sign In')
    return render(request,'registration/signin.html')

