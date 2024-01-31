from django.shortcuts import render

from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    


#working on views which has been already setup for us using rest_framework



# from django.http import HttpResponse

# # Create your views here.
# # ceating my own end_points

# def main(request):
#     return HttpResponse("Hello")