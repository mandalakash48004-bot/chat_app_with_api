from email.policy import default

from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name= models.CharField(max_length=1000)

class Message(models.Model):
    value= models.CharField(max_length=1000000) ### value means the message that user will send..like how are you,etc.
    date= models.DateTimeField(default=datetime.now) ### date means the time when user will send the message.
    user= models.CharField(max_length=1000000) ### user means the name of the user who will send the message.
    room= models.CharField(max_length=1000000)    ### room means the name of the room where user will send the message.