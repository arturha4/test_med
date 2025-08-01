from rest_framework import generics
from .models import ClientTovar
from .serializers import ClientTovarSerializer

class ClientTovarListAPIView(generics.ListAPIView):
    queryset = ClientTovar.objects.all()
    serializer_class = ClientTovarSerializer
