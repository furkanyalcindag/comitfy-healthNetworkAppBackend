from django.db import models
from healthApp.models.BaseModel import BaseModel
from healthApp.models.Category import Category
from healthApp.models.Sponsor import Sponsor

class ChatRoom(BaseModel):
    name = models.CharField(max_length=256, null=False)
    description = models.CharField(max_length=256, null=True)
    max_users = models.IntegerField(default=1000000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    isSponsored = models.BooleanField(default=False)
    sponsor = models.ForeignKey(Sponsor,on_delete=models.CASCADE,null=True)

