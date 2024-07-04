from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from .models import Movies,User
from rest_framework import status
from .serializers import MoviesSerializers , UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView #module
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,TokenAuthentication





@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        token = RefreshToken.for_user(user)
        return Response({"refresh": str(token), "access": str(token.access_token)})
    return Response(serializer.errors, status=400)

 

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({"details": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    token = RefreshToken.for_user(user)
    serializer = UserSerializer(user)
    return Response({"token": str(token.access_token), "user": serializer.data})


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def test_token(request):
        return Response({"message": "Token authentication successful", "username": request.user.username}) 

#########################################################################################################################################
@api_view(['GET'])
def get_Movies(request):
    
        movies = Movies.objects.all()
        serializer = MoviesSerializers(movies,many=True)
        # return Response({'status':200,'payload':serializer1.data})
        return Response(serializer.data)

@api_view(['POST'])
def create_Movies(request):
    serializer = MoviesSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_Movies(request, pk):
    try:
        movies = Movies.objects.get(pk=pk)
    except Movies.DoesNotExist:
        return Response({'error': 'Movies not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = MoviesSerializers(Movies, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_Movies(request, pk):
    try:
        movies = Movies.objects.get(pk=pk)
    except movies.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    
    movies.delete()
    return Response({'message': 'Movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    