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
    
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
