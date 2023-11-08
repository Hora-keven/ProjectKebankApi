import statistics
from flask import Response
from rest_framework import viewsets
from Kebank.Api.serializers import *
from Kebank.models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class PhysicalPersonViewSet(viewsets.ModelViewSet):
    serializer_class = PhysicalPersonSerializer
    queryset = PhysicalPerson.objects.all()
    
class JuridicPersonViewSet(viewsets.ModelViewSet):
    serializer_class = JuridicPersonSerializer
    queryset = JuridicPerson.objects.all()
    
class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    
    def create(self, request, *args, **kwargs):
        data = request.data
        account = Account(
          agency = 5434,
          number = number_random(100000000, 900000000),
          number_verificate =number_random(1, 5),
          type_account=data["type_account"],
          limit = number_random(300, 1000000),
          physical_person = data["physical_person"],
      )
        account.save()
        return account    
    
class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerialzer
    queryset = Address.objects.all()
    
class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset=Card.objects.all()
    
    def create(self, request, *args, **kwargs):
        number = number_random(a=1000000000000, b=10000000000000)
        data = request.data
        card = Card(
        account = data["account"],
        flag_card = "Mastercard",
        number = str(number)+"0810",
        validity = "12/2035",
        cvv = number_random(a=100, b=900)
        )
        card.save()
        return card 

class LoanViewSet(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

class MovimentationViewSet(viewsets.ModelViewSet):
    serializer_class = MovimentationSerializer
    queryset = Movimentation.objects.all()
    
class PixViewSet(viewsets.ModelViewSet):
    serializer_class = PixSerializer
    queryset = Pix.objects.all()
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class InvestmentViewSet(viewsets.ModelViewSet):
    serializer_class = InvestmentSerializer
    queryset = Investment.objects.all()
    

