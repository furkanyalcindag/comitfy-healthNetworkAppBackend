from django.contrib.auth.models import User
from django.db import models

from healthApp.models.BaseModel import BaseModel
from healthApp.models.Gender import Gender

from healthApp.models.Nationality import Nationality


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage = models.TextField(null=True, blank=True)
    mobilePhone = models.CharField(max_length=20, null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    birthDate = models.DateField(null=True)
    birthYear = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    district = models.CharField(max_length=64, blank=True, null=True)
    notification = models.BooleanField(default=True)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    isSendMail = models.BooleanField(default=False)