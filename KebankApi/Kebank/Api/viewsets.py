from rest_framework import serializers
from django.db.models import fields
from Kebank.models import *
from Kebank.Api.number_rand import *
from datetime import datetime, timedelta

import pytz

date_actual = datetime.now(pytz.utc)

date_future = date_actual + timedelta(days=365 * 5)

fuso_horario = pytz.timezone('America/Sao_Paulo')

date_future_timezone = date_future.astimezone(fuso_horario)



class AddressSerialzer(serializers.ModelSerializer):

    class Meta:
      model = Address
      fields = "__all__"
  

      
class CardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Card
    fields = "__all__"
  
  def to_internal_value(self, data):
      
        return {
            'account': Account.objects.get(id=data['account']),
            'flag_card': 'Mastercard',
            'number': str(number_random(a=100000000000, b=1000000000000))+"0810",
            'validity': date_future_timezone.date(),
            'cvv': number_random(100, 900),  
        }

  def create(self, validated_data):
       
        return Card.objects.create(**validated_data)

  
    
      
class LoanSerializer(serializers.ModelSerializer):
  class Meta:
    model = Loan
    fields = "__all__"
  
class PixSerializer(serializers.ModelSerializer):
    
    class Meta:
      model = Pix
      fields = ["to_account",  "from_account", "value"]

   
    

class AccountSerializer(serializers.ModelSerializer):
    account_card = CardSerializer(many=True, read_only=True)
  
    physical_name = serializers.SerializerMethodField()
    juridic_name = serializers.SerializerMethodField()
    
    class Meta:
      model = Account
      fields = ["id","physical_name", "juridic_name", "account_card", "physical_person", "agency", "number", "limit","juridic_person","number_verificate","type_account" ]

    def get_physical_name(self, obj):
        physical_person = getattr(obj, 'physical_person', None)

        if physical_person:
            user = physical_person.fk_user
            return {'id': user.id, 'first_name': user.first_name}
        
        else:
            return None
          
    def get_juridic_name(self, obj):
        juridic_person = getattr(obj, 'juridic_person', None)

        if juridic_person:
            user = juridic_person.fk_user
            return {'id': user.id, 'first_name': user.first_name}
        
        else:
            return None
        
    def create(self, validated_data):
        physical_person = validated_data.pop('physical_person') 
        juridic_person = validated_data.pop("juridic_person")
        
        instance_physical_person = Account.objects.create(**physical_person)
        instance_juridic_person =  Account.objects.create(**juridic_person)
        
        validated_data['physical_person'] = instance_physical_person
        validated_data['juridic_person'] = instance_juridic_person

        if physical_person:
          
          return instance_physical_person
        else:
          return instance_juridic_person
        

  
    
class MovimentationSerializer(serializers.ModelSerializer):
    date_hour = serializers.SerializerMethodField()
    account = serializers.SerializerMethodField()
    class Meta:
      model = Movimentation
      fields = "__all__"

  
    def get_date_hour(self, instance):
    
        return instance.date_hour.strftime('%d/%m/%Y %H:%M:%S')   
      
    
    def get_account(self, obj):
        user = getattr(obj, 'account', None)
        
        if user.physical_person:
            user = user.physical_person
            return {'cpf': user.cpf, 'name': user.fk_user.first_name}
        elif user.juridic_person:
            user = user.juridic_person
            return {'cnpj': user.cnpj, 'Company_name': user.fk_user.first_name}
        else:
          return None
      
class PhysicalPersonSerializer(serializers.ModelSerializer):
   
    user = serializers.SerializerMethodField()
  
    class Meta:
        model = PhysicalPerson
        fields = [  "cpf", "rg","born_date", "user", "fk_user"]

    def get_user(self, obj):
        user = obj.fk_user
        return {'id': user.id, 'first_name': user.first_name}

class JuridicPersonSerializer(serializers.ModelSerializer):

  
  class Meta:
        model = JuridicPerson
        fields = "__all__"
    
class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
      model = Investment
      fields = "__all__"

class CreditCardSerializer(serializers.ModelSerializer):
   class Meta:
      model=CreditCard
      fields = "__all__"

      write_only_fields = "account"
      
    
    
    
      

      
      
  

  
        
        
        
