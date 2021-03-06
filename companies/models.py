from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image
from io import BytesIO
from django.core.files import File


def compress(image, quality=20):
    im_io = BytesIO()
    im = Image.open(image)
    if im.mode != 'RGB' or not image:
        im = im.convert('RGB')
        im.save("media/test.jpg")
    im.save(im_io, 'JPEG', quality=quality)
    new_image = File(im_io, name=image.name)
    return new_image


class Company(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
    )
    company_name = models.CharField(max_length=50)
    profile_photo = models.ImageField(blank=True)
    background_photo = models.ImageField(blank=True)
    short_description = models.CharField(max_length=150)
    description = models.TextField()
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        self.profile_photo = compress(self.profile_photo)
        self.background_photo = compress(self.background_photo, 40)
        super().save(*args, **kwargs)
