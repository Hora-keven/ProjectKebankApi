from rest_framework import viewsets
from Kebank.Api.serializers import LegalPersonSerializer, UserSerializer
from Kebank.models import *

class LegalPersonViewSet(viewsets.ModelViewSet):
    serializer_class = LegalPersonSerializer
    queryset = LegalPerson.objects.all()
    
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()