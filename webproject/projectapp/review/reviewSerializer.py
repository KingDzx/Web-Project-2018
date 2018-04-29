from . import Review
from rest_framework import serializers

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('id','firstname','lastname','rating','message','services') 