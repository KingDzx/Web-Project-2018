from . import Worker
from rest_framework import serializers

class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Worker
<<<<<<< HEAD
        fields = ('id','first_name','last_name','username','password')
=======
        fields = ('id','first_name','last_name','username','password')
>>>>>>> 09c7e9e335226e37f264c249c7242461ae9c5439
