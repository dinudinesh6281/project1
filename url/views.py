from django.shortcuts import render

from django.http import HttpResponse

def longboat(request):
    return HttpResponse("this is good place for drinks")

