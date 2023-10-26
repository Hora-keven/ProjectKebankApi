from rest_framework import viewsets
from Kebank.Api.serializers import *
from Kebank.models import *

class LegalPersonViewSet(viewsets.ModelViewSet):
    serializer_class = LegalPersonSerializer
    queryset = LegalPerson.objects.all()
    
class JuridicPersonViewSet(viewsets.ModelViewSet):
    serializer_class = JuridicPersonSerializer
    queryset = JuridicPerson.objects.all()
    
class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    