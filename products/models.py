from django.contrib.auth.models import User
from django.db import models



class BotType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT, related_name='owner')
    allowed_users = models.ManyToManyField(User, blank=True, related_name='allowed')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "BotType"


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
    bot = models.ForeignKey(BotType, on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date_created"]
        verbose_name_plural = "Items"


