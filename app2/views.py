from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
def one(request):
    return HttpResponse('<h1><marquee>WE ARE ALWAYS GOOD</marquee></h1>')
def two(request):
    return HttpResponse('<h1><marquee>THIS IS MY LAST PROJECT WORK</marquee></h1>')
