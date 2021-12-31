
from django.db import models
from healthApp.models.BaseModel import BaseModel

class Gender(BaseModel):
    keyword = models.CharField(max_length=24, null=True)