from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User
from .validators import RegisterValidator
from django.core.exceptions import ValidationError




class NoteSerializer(ModelSerializer):
    

    class Meta:
        model = Note
        fields = '__all__'



    def create(self,validated_data):

        body = validated_data.get('body')
        user_object = validated_data.get('user')
        object_note = Note.objects.create(body=body,user=user_object)

        return object_note


    def update(self, instance, validated_data):
        body = validated_data.get('body', instance.body)  
        check = validated_data.get('done',instance.done)
        print(check)
        instance.body = body
        instance.done = check
        instance.save()
        return instance
    


class RegistrationSerializer(serializers.Serializer):
    
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    repeat_password = serializers.CharField(write_only=True)
    # access_token = serializers.CharField(read_only=True)
    # refresh_token = serializers.CharField(read_only=True)



    def validate(self, attrs):
        
        validator = RegisterValidator(attrs)
        validator.run_validate()

        if validator.is_validate:
            return attrs
        

        raise ValidationError(validator._errors)
    



    def create(self, validated_data):
        
        username = validated_data.get('username')
        password = validated_data.get('password')

        user = User.objects.create(username=username)
        user.set_password(password)

        user.save()
        


        return user