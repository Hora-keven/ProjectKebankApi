from django.shortcuts import get_object_or_404
from rest_framework import serializers
from Kebank.models import *
from Kebank.Api.number_rand import *
from decimal import Decimal

class PhysicalPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalPerson
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
    
      account = Account(
          agency = 5434,
          number = number_random(100000000, 900000000),
          number_verificate =number_random(1, 5),
          type_account=validated_data["type_account"],
          limit = number_random(300, 1000000),
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
    number = number_random(a=1000000000000, b=10000000000000)

    card = Card(
       account = validated_data["account"],
       flag_card = "Mastercard",
       number = str(number)+"0810",
       validity = "12/2035",
       cvv = number_random(a=100, b=900)
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
  
  
class PixSerializer(serializers.ModelSerializer):
    class Meta:
      model = Pix
      fields = "__all__"
      
    def create(self, validated_data):
      pix = Pix(
        from_account = validated_data["from_account"],
        value = validated_data["value"],
        to_account = validated_data["to_account"]
      )
      
      if pix.value > pix.from_account.limit:
          raise serializers.ValidationError("Value is bigger than your limit")
        
      else:
        pix.from_account.limit -= pix.value
        pix.to_account.limit += pix.value
        
        pix.from_account.save()
        pix.to_account.save()
        pix.save()
        
        movimetation_from = Movimentation(
          value = (-pix.value),
          card = Card.objects.get(account = pix.from_account),
          state = "sent"
        )
        movimetation_to= Movimentation(
          value = pix.value,
          card = Card.objects.get(account = pix.to_account),
          state = "received"
        )
        
        movimetation_from.save()
        movimetation_to.save()
        
      return pix
    
class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
      model = Investment
      fields = "__all__"
      
    def create(self, validated_data):
      
      investment = Investment(
          contribuition = validated_data["contribuition"],
          investment_type = "Fixa",
          rentability = "1.37",
          date_closure = validated_data["date_closure"],
          income = "0.00",
          account = validated_data["account"],
          administration_fee = "0.30"
          
      )
      if investment.contribuition >  investment.account.limit:
        raise serializers.ValidationError("Contribuition is more than limit")
      
      else:
        movimetation = Movimentation(
          value = (-investment.contribuition),
          card = Card.objects.get(account = investment.account),
          state = "Investment successfully"
        )
        movimetation.save()
        investment.account.limit -= investment.contribuition
        investment.account.save()
        investment.save()
        
        
        
      return investment

      
      
  

  
        
        
        
