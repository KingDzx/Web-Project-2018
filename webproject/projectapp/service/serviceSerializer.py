from . import Service
from rest_framework import serializers

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('id','name','service','address','description','reviews')