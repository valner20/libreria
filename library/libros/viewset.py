from rest_framework.viewsets import ModelViewSet
from .models import Libro
from .serializers import LibroSerializer   

class LibroViewset(ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer 
