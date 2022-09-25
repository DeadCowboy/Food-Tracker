from django.db import models

# Create your models here.

class BarcodeItem(models.Model):
    BarcodeNumber = models.PositiveIntegerField(blank=True)
    Image = models.ImageField()
    WheightOfNewPackage = models.PositiveIntegerField()
    WheightCurrentlyInStorage = models.PositiveIntegerField()
    NumberOfItemsInNewPackage = models.PositiveIntegerField(default=1)
    NumberOfItemsCurrentlyInStorage = models.PositiveIntegerField()
