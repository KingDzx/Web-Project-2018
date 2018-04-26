from . import Worker
from rest_framework import serializers

class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Worker
<<<<<<< HEAD
        fields = ('id','first_name','last_name','username','password')
=======
        fields = ('id','name','service','address','description')
>>>>>>> 98e27fde1844552500715dbe10a963ea2ef74657
