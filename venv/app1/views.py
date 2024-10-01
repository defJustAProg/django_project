from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello from app1")

def url2(request):
    return HttpResponse("url2 from app1")

def url3(request):
    return HttpResponse("url3")