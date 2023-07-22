from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def one(request):
    return HttpResponse('<h1>THIS IS MY FIRST PROJECT IN DJANGO</h1>')
def two(request):
    return HttpResponse('<h1><marquee>THIS IS MY LIFE TIME ERNINGS</marquee></h1>')
