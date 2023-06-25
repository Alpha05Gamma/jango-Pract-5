from django.db import models

# Create your models here.

class Enemy(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    picture = models.ImageField()
    health = models.IntegerField()
    loot = models.CharField(max_length=100)
    runes = models.IntegerField()
    location = models.CharField(max_length=100)

class Boss(models.Model):
    Enemy = models.ForeignKey(Enemy, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    pattern =  models.CharField(max_length=800)

class NPC(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    picture = models.ImageField()
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    picture = models.ImageField()
    description = models.CharField(max_length=500)
    cost = models.CharField(max_length=120)

class Weapon(models.Model):
    Item =  models.ForeignKey(Item, on_delete=models.CASCADE)
    damage_types = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    skill = models.CharField(max_length=500)


class Player(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=5)
    rating = models.IntegerField()
    def __str__(self):
        return f'{self.name, self.region, self.rating}'