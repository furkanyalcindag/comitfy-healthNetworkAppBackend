from django.db import models
from healthApp.models.BaseModel import BaseModel



class Category(BaseModel):
    keyword = models.CharField(max_length=256)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
