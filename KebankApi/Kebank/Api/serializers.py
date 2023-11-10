from rest_framework import serializers

from Kebank.models import *
from Kebank.Api.number_rand import *


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
    
    
      

      
      
  

  
        
        
        
