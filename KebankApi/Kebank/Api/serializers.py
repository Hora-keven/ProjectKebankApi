from rest_framework import serializers
from django.shortcuts import get_object_or_404
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
      
class LoanSerializer(serializers.ModelSerializer):
  class Meta:
    model = Loan
    fields = "__all__"
  
  
  
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
        movimentation = Movimentation(
          value = (-investment.contribuition),
          account = Card.objects.get(account = investment.account.id),
          state = "Investment successfully"
        )
     
    
        movimentation.save()
        investment.account.limit -= investment.contribuition
        investment.account.save()
        investment.save() 
        
      return investment
    
    
      

      
      
  

  
        
        
        
