


from django.db import models
from healthApp.models.BaseModel import BaseModel
from healthApp.models.Language import Language
from healthApp.models.Profile import Profile


class Article(BaseModel):
    keyword = models.CharField(max_length=128, default=True, blank=True)
    title = models.CharField(max_length=128)
    date = models.DateField()
    article = models.TextField()
    doctor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)