from django.db import models
from healthApp.models.Article import Article
from healthApp.models.BaseModel import BaseModel
from healthApp.models.Profile import Profile

class ArticlePin(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile)

