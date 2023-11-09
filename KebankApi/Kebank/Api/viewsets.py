
from rest_framework import viewsets, status, filters
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
    
    def get_queryset(self):
        pk = self.kwargs["pk"]
      
        physical_person = PhysicalPerson.objects.get(cpf=pk)
        queryset = Account.objects.filter(physical_person=physical_person)
        
        return queryset
    
    def list(self, request, *args, **kwargs):
        query_set = Account.objects.all()
        data = AccountSerializer(data=query_set, many=True)
      
        if data.is_valid():
            return Response(data=data.data, status=status.HTTP_400_BAD_REQUEST)
        else:
           return Response(data=data.data, status=status.HTTP_200_OK)
      
    def create(self, request, *args, **kwargs):
        data = request.data
      
        account = Account(
          agency = 5434,
          number = number_random(100000000, 900000000),
          number_verificate =number_random(1, 5),
          type_account=data["type_account"],
          limit = number_random(300, 1000000),
          physical_person = PhysicalPerson.objects.get(cpf=data["physical_person"]),
        )
        account_serializer = self.serializer_class(data=data)
        
        if account_serializer.is_valid():
            account.save()
            return Response(data=account_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=account_serializer.data, status=status.HTTP_400_BAD_REQUEST)

       
    
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
        card_serializer = self.serializer_class(data=data)
        
        if card_serializer.is_valid():
            card.save()
            return Response(data=card_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=card_serializer.data, status=status.HTTP_400_BAD_REQUEST)

class LoanViewSet(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
    
    def create(self, request, *args, **kwargs):
        data = request.data
        loan = Loan(
        account =Account.objects.get(id=data["account"]),
        requested_amount = Decimal(data["requested_amount"]),
        approved = False,
        installment_quantity = data["installment_quantity"]
        )
        
        if loan.installment_quantity == 12 and loan.account.limit >= loan.requested_amount:
            loan.fees = Decimal(0.50)
            loan.account.limit -= loan.requested_amount*loan.fees 
            loan.approved = True 

        elif loan.installment_quantity == 24 and loan.account.limit >= loan.requested_amount:
            loan.fees = Decimal(0.60)
            loan.account.limit -= loan.requested_amount*loan.fees 
            loan.approved = True 

        elif loan.installment_quantity == 24 and loan.account.limit >= loan.requested_amount:
            loan.fees = Decimal(0.8)
            loan.account.limit -= loan.requested_amount*loan.fees
            loan.approved = True 

        else:
            raise serializers.ValidationError("Loan not approved")
        

        movimentation = Movimentation(
            value = loan.requested_amount,
            account = Account.objects.get(id=loan.account.id),
            state = "loan successfully"
        )
        
      
        
        loan_serializer = LoanSerializer(data=data)
        if loan_serializer.is_valid():
            movimentation.save()
            loan.save() 
            loan.account.save()
            
            return Response(data=loan_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=loan_serializer.data, status=status.HTTP_400_BAD_REQUEST)
   
   

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
    

