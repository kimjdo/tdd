from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return HttpResponse('<html><title>일정관리</title><body><h1>hi</h1></body></html>')
