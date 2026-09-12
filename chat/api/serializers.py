from rest_framework import serializers
from chat.models import Room,Message

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=['name']


class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=['value','date','user','room']
        
