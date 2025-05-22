from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Author, AuthorLibros, registro
from .serializers import AuthorSerializer, AuthorLibrosSerializer, RegistroSerializer, UserSerializer   



class  AuthorViewset(ModelViewSet):
    queryset= Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Author.objects.filter(datos = self.request.user)
    

class  AuthorLibrosViewset(ModelViewSet):
    queryset= AuthorLibros.objects.all()
    serializer_class =  AuthorLibrosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AuthorLibros.objects.filter(autor__datos = self.request.user )
    
    def perform_create(self, serializer):
        autor = serializer.validated_data['autor']
        if autor != self.request.user:
            raise PermissionDenied("No puedes usar este autor.")
        
        libro = serializer.validated_data['libro']
        if libro.author != autor:
            raise PermissionDenied("Este libro no pertenece al autor.")

        serializer.save()


class registroViewset(viewsets.ViewSet):
    queryset= registro.objects.all()
    serializer_class = RegistroSerializer

    def create(self, request):
        serializer = RegistroSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    def list(self,request):
        serializer = RegistroSerializer()
        return Response(serializer.data)
        
class UserViewset(ModelViewSet):
     queryset = User.objects.all()
     serializer_class = UserSerializer


    
