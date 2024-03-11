from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from greeting.models import add_details
from .serializers import add_detailsSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import userSerializer
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from greeting.forms import addmedicine
from rest_framework import status
# Create your views here.

#read medicine
@api_view(['GET'])
@permission_classes((AllowAny,))
def getdata(request):
    items=add_details.objects.all()
    serializer=add_detailsSerializer(items,many=True)
    return Response(serializer.data)  

#add medicine 
@api_view(['POST'])
@permission_classes((AllowAny,)) 
def postdata(request):
    serializer=add_detailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("account created successfully")
    return Response(serializer.errors)


#signup form 
@api_view(['POST'])
@permission_classes((AllowAny,)) 
def signup(request):
    serializer=userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("account created successfully")
    return Response(serializer.errors)

#login form
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)


#update data
@api_view(['PUT'])
@permission_classes((AllowAny,))
def update(request, id):
    product = get_object_or_404(add_details, pk=id)
    form = addmedicine(request.data, instance=product)
    if form.is_valid():
        form.save()
        serializer = add_detailsSerializer(product)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    

#delete data
@api_view(['DELETE'])
@permission_classes((AllowAny,))
def delete(request, id):
    try:
        product = add_details.objects.get(pk=id)
    except add_details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response("deleted successfully")