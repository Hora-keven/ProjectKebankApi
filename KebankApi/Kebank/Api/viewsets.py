import statistics
from flask import Response
from rest_framework import viewsets
from Kebank.Api.serializers import *
from Kebank.models import *

class PhysicalPersonViewSet(viewsets.ModelViewSet):
    serializer_class = PhysicalPersonSerializer
    queryset = PhysicalPerson.objects.all()
    
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

class MovimentationViewSet(viewsets.ModelViewSet):
    serializer_class = MovimentationSerializer
    queryset = Movimentation.objects.all()
    
class PixViewSet(viewsets.ModelViewSet):
    serializer_class = PixSerializer
    queryset = Pix.objects.all()
    
class InvestmentViewSet(viewsets.ModelViewSet):
    serializer_class = InvestmentSerializer
    queryset = Investment.objects.all()
    