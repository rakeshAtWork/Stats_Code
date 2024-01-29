from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# ceating my own end_points

def main(request):
    return HttpResponse("Hello")