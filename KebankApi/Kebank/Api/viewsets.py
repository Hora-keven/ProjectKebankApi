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
    
class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerialzer
    queryset = Address.objects.all()
    
class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset=Card.objects.all()
    
class LoanViewSet(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
    