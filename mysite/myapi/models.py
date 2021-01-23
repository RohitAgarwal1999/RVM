# models.py
from django.db import models
class employ(models.Model):
    name = models.CharField(max_length=60)
    sirname = models.CharField(max_length=60)
    def __str__(self):
        return self.name