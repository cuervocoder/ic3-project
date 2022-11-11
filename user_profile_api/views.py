from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from django.http import Http404
from user_profile_api import serializers, models, permissions, services
from users_admin.settings import ENVIRONMENT
from io import StringIO
import json

# Create your views here.
def transform_response(response):
    if ENVIRONMENT == 'PROD':
        return response.data
    else:
        io = StringIO(response.data)
        
        return json.load(io)

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        hello_apiview = [
            'Usamos metodos HTTP como funciones (get, post, put, delete)',
            'Esto es una prueba',
            'Mapea manualmente los URLs'
        ]

        return Response({'message': 'Hello', 'hello_apiview': hello_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})

class UserProfileApiView(APIView):
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    def get(self, request, format=None, *args, **kwargs):
        res = services.search_users()

        if res.status_code >= 300:
            raise ValueError('Error perform search!')
        else:
            r = transform_response(res)
            
            print(r['UserInfoSearch'])

            users = models.UserProfile.objects.all()
            serializer = serializers.UserProfileSerializer(users, many=True)
            
            return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            res = services.record_user(serializer)

            if res.status_code >= 300:
                raise ValueError('Error perform record!')
            else:                
                print("Hola test", res)
                print('Esto es', serializer.validated_data)
                begin_time = serializer.validated_data["begin_time"]
                begin_time_final = begin_time.strftime("%Y-%m-%dT%H:%M:%S")
                print(begin_time_final)
                      
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileApiViewDetail(APIView):
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    def get_object(self, pk):
        try:
            return models.UserProfile.objects.get(pk=pk)
        except models.UserProfile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = self.serializer_class(user)

        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = self.serializer_class(user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
