from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .models import Note,User
from .serializers import NoteSerializer,RegistrationSerializer
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import jwt




class NotesRetriew(APIView):



    def get(self,request):

        auth_header = request.headers.get('Authorization')

        auth_token = auth_header.split(' ')[1]

        payload = jwt.decode(auth_token, algorithms=['RS256'], options={"verify_signature": False})
        user_username = payload['user']



        notes = Note.objects.filter(user__username=user_username)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    


    

class NoteCreate(APIView):

    @extend_schema(request=NoteSerializer, responses={'200': NoteSerializer})
    def post(self,request):


        user_username= request.data.get('user')['user']
        body = request.data.get('body')

        user_object = User.objects.get(username=user_username)


        data = {
            'user': user_object.id,  
            'body': body
                }


        serializer = NoteSerializer(data=data)

        if serializer.is_valid():


            serializer.save()

            return Response(serializer.data)
        
        return Response({'error':'something_wrong'},status=status.HTTP_400_BAD_REQUEST)




class NoteGetOne(APIView):



    def get(self,request,pk):

        notes = Note.objects.get(id=pk)
        serializer = NoteSerializer(notes, many=False)
        return Response(serializer.data)

        
class NoteChangeOne(APIView):

    @extend_schema(request=NoteSerializer, responses={'200': NoteSerializer})
    def put(self,request,pk):
        data = request.data
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(instance=note, data=data)

        if serializer.is_valid():
             serializer.save()

        return Response(serializer.data)


class NoteDeleteOne(APIView):


    def delete(self,request,pk):

        user_username= request.data.get('user')['user']
        user_object = User.objects.get(username=user_username)


        note = Note.objects.get(id=pk)
        note.delete()

        try:
            note = Note.objects.get(id=pk)
        except Note.DoesNotExist:
            return Response(status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    



class RegistrationApiView(APIView):

    def post(self, request):


        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            user = serializer.save()

            return Response({"message": "Пользователь успешно зарегистрирован."})
        
        print (serializer._errors)
        
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

















class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['user'] = user.username
        # ...

        return token
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer