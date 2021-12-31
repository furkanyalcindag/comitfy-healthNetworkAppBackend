from django.db import models
from django.db.models.deletion import CASCADE
from healthApp.models.BaseModel import BaseModel
from healthApp.models.Profile import Profile

class Gallery(BaseModel):
    name = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
