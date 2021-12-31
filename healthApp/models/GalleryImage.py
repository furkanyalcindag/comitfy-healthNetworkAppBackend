from django.db import models
from healthApp.models.BaseModel import BaseModel
from healthApp.models.Gallery import Gallery


class GalleryImage(BaseModel):
    image = models.ImageField(upload_to='photos', max_length=254)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)