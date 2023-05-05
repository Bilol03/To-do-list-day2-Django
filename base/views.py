from django.shortcuts import render
from django.http import HttpResponse

def list(response):
    return HttpResponse("To do list")