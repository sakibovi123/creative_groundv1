from typing import Text
from django.db import models


class BackGroundImage(models.Model):
    image_file = models.ImageField(upload_to="images/")

    def __str__(self):
        return str(self.id)


class TextElements(models.Model):
    content = models.TextField()

    def __str__(self):
        return str(self.id)


class MoreImages(models.Model):
    images_field2 = models.ImageField(upload_to="images/", null=True, blank=True)


    def __str__(self):
        return str(self.id)


class OfferImage(models.Model):
    slug = models.SlugField(unique=True)
    background_image = models.ForeignKey(BackGroundImage, on_delete=models.DO_NOTHING)
    main_text = models.ManyToManyField(TextElements)
    extra_images = models.ManyToManyField(MoreImages)







