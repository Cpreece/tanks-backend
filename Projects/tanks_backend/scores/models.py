from django.db import models

# Create your models here.

class Scores(models.Model):
    user = models.CharField(max_length=20)
    level = models.IntegerField()
    tanks_destroyed = models.IntegerField()
    seconds_survived = models.IntegerField()
    missiles_fired = models.IntegerField()
