from django.db import models
from django.utils import timezone


class Item(models.Model):
    FRANCE = 'Fr'
    USA = 'US'
    RUSSIA = 'Ru'
    CHINA = 'CH'

    COUNTRIES_CHOICES = [
        (FRANCE, 'France'),
        (USA, 'USA'),
        (RUSSIA, 'Russia'),
        (CHINA, 'China'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    article = models.IntegerField()
    price = models.DecimalField(max_digits=4,decimal_places=2)
    country = models.CharField(choices=COUNTRIES_CHOICES, max_length=150)
    color = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photo_item', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date_created"]
        verbose_name_plural = "Items"
