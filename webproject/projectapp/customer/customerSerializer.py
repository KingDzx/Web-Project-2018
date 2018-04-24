from . import Customer
from rest_framework import serializers

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','first_name','last_name','username','password')