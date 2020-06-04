from rest_framework import generics
from .serializers import JoinSerializer
from newsletter.models import Join

class JoinCreateAPIView(generics.CreateAPIView): 
    queryset = Join.objects.all()
    serializer_class = JoinSerializer
    permission_classes = []
    authentication_classes = []