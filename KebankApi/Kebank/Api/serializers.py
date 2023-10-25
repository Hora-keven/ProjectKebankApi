from rest_framework import serializers
from Kebank.models import *
class LegalPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalPerson
        fields = "__all__"
        
class UserSerializer(serializers.ModelSerializer):
      class Meta:
        model = User
        fields = "__all__"
        
        
        
