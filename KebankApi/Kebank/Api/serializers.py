from rest_framework import serializers
from Kebank.models import *
import random
class LegalPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalPerson
        fields = "__all__"

        
    legal_person = serializers.StringRelatedField()
        
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
      number = 0
      number_verificate = 0
      
      for i in range(9):
        number = random.randint(b=900000000, a=100000000)
        number_verificate = random.randint(b=5, a=1)
        
      account = Account(
          agency = agency,
          number = number,
          number_verificate = number_verificate,
          type_account=validated_data["type_account"],
          limit = validated_data["limit"],
          legal_person = validated_data["legal_person"],
       
      )
    
      account.save()
        
      return account
      
  

  
        
        
        
