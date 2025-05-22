from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author,AuthorLibros, registro
from libros.models import Libro
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ["alias","date_start","cantidad_libros"]

    def create(self, validated_data):
        user = self.context['request'].user
        return Author.objects.create(datos = user, **validated_data)

class AuthorLibrosSerializer(serializers.ModelSerializer):
    autor = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = AuthorLibros
        fields = "__all__"  
    
    
   

class RegistroSerializer(serializers.ModelSerializer):
    telefono = serializers.CharField(write_only=True)
    direccion = serializers.CharField(write_only=True) 
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'direccion','telefono']   

    def create(self, validated_data):
        telefono = validated_data.pop('telefono')
        password = validated_data.pop('password')
        direccion = validated_data.pop('direccion')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        registro.objects.create(user=user, telefono=telefono, direccion = direccion)
        return user
    

        
