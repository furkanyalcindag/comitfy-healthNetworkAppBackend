
from django.db import models
from healthApp.models.BaseModel import BaseModel
from healthApp.models.Profile import Profile
from healthApp.models.ChatRoom import ChatRoom

class ChatMessage(BaseModel):
    fromUser = models.ForeignKey(Profile, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    replyTo = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
