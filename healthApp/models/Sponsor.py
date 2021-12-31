from django.db import models
from healthApp.models.BaseModel import BaseModel
class Sponsor(BaseModel):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='sponsor', max_length=254)
    website = models.CharField(max_length=255, null=True)

