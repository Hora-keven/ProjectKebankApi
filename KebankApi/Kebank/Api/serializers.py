from rest_framework import serializers
from Kebank.models import *
import random
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
    true_false = random.randint(a=0, b=1)
    aprroved_or_no = [False, True]
    aprroved = aprroved_or_no[true_false]
    
    loan = Loan(
      account = validated_data["account"],
      requested_amount = validated_data["requested_amount"],
      approved = aprroved,
      installment_quantity = validated_data["installment_quantity"]
    )
    
    if loan.installment_quantity == 12:
        loan.fees = 0.5
    elif loan.installment_quantity == 24:
        loan.fees = 0.6
    else:
      loan.fees = 0.8
   
  
    balance = Account.objects.get(id=int(validated_data["account"]))
    balance.limit = loan.fees*validated_data["requested_amount"]
    balance.save()
    loan.save() 
    return loan

      
      
  

  
        
        
        
