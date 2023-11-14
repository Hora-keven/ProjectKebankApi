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
      
    
    
    
      

      
      
  

  
        
        
        
