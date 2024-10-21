from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'dashboard/home.html')
    ## return HttpResponse('This is the Home Page')

def recentActivity(request):
    return render(request,'dashboard/recentActivity.html')


 