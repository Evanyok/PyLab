from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")

def detail(request, uid):
    return HttpResponse("detail")

def results(request):
    return HttpResponse("results")
