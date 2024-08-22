from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes , throttle_classes
from rest_framework.throttling import AnonRateThrottle
from .serializers import MenuItemSerializer
from .models import MenuItem
# Create your views here.

@api_view()
def books(request):
    return Response('list of the books',status= status.HTTP_200_OK)



class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer



@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"Some secret message"})
@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if  request.user.groups.filter(name = 'Manager').exists():
        return Response({"message":"Only Manager should see this "})
    
    return Response({"message":"You are not authorized :( ) "},403)

@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return  Response({"message":"success"})
