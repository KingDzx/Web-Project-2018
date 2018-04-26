from . import Worker
from rest_framework import serializers

class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Worker
        fields = ('id','first_name','last_name','username','password')