from django.db import models
from healthApp.models.BaseModel import BaseModel
from healthApp.models.Category import Category
from healthApp.models.Language import Language

class GenderDescription(BaseModel):
    name =   models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)