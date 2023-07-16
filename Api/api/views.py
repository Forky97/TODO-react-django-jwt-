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
from .utils import Utils




class NotesRetriew(APIView):



    def get(self,request):


        ### if no swagger  off : 

        username_from_token = Utils.get_user_from_token(data=request)



        notes = Note.objects.filter(user__username=username_from_token)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
       ### if swagger on 



        # notes = Note.objects.all()
        # serializer = NoteSerializer(notes, many=True)
        # return Response(serializer.data)


    

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
    def patch(self,request,pk):




        note_to_change = Note.objects.get(id=pk)
        note_owner = note_to_change.user


        #### need to add authorization tokens frontend to header 


        username_from_token = Utils.get_user_from_token(data=request)



        if str(note_owner) == username_from_token:

            request.data['user'] = note_owner.id



            serializer = NoteSerializer(instance=note_to_change, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                return Response(request.data)

        else:


            return Response({'status' : 'bad_request_400'})




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