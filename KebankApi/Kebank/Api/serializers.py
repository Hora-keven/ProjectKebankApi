from django.shortcuts import get_object_or_404
from rest_framework import serializers
from Kebank.models import *
import random
from decimal import Decimal
class LegalPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalPerson
        fields = "__all__"

class JuridicPersonSerializer(serializers.ModelSerializer):
  class Meta:
        model = JuridicPerson
        fields = "__all__"
        
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
      model = Account
      fields = "__all__"
      
    def create(self, validated_data):
      agency = 5434
      number = random.randint(b=900000000, a=100000000)
      number_verificate = random.randint(b=5, a=1)
      limit = random.randint(a=300,b=1000000)
        
      account = Account(
          agency = agency,
          number = number,
          number_verificate = number_verificate,
          type_account=validated_data["type_account"],
          limit = limit,
          legal_person = validated_data["legal_person"],
      )
    
      account.save()
        
      return account
    
class AddressSerialzer(serializers.ModelSerializer):
    class Meta:
      model = Address
      fields = "__all__"
      
      
class MovimentationSerializer(serializers.ModelSerializer):
    class Meta:
      model = Movimentation
      fields = "__all__"
      
    def create(self, validated_data):
       return super().create(validated_data)
     
class CardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Card
    fields = "__all__"
    
  def create(self, validated_data):
    number = random.randint(a=1000000000000, b=10000000000000)
    cvv = random.randint(a=100, b=900)
    number_str = str(number)+"0810"
    
    card = Card(
       account = validated_data["account"],
       flag_card = "Mastercard",
       number = number_str,
       validity = "12/2035",
       cvv = cvv
     )
    card.save()
    
    return card
      
      
class LoanSerializer(serializers.ModelSerializer):
  class Meta:
    model = Loan
    fields = "__all__"
  
    
  def create(self, validated_data):
  
    loan = Loan(
      account = validated_data["account"],
      requested_amount = validated_data["requested_amount"],
      approved = False,
      installment_quantity = validated_data["installment_quantity"]
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
        card = Card.objects.get(account=loan.account),
    )
    
    movimentation.save()
    loan.save() 
    loan.account.save()
    return loan

      
      
  

  
        
        
        
