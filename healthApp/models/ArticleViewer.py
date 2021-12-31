from django.db import models
from healthApp.models.BaseModel import BaseModel
from healthApp.models.Profile import Profile
from healthApp.models.Article import Article


class ArticleViewer(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    reader = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    isFromAdvertisement = models.BooleanField(default=False)
