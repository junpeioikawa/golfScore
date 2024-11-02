from django.db import models
from django.utils import timezone
from golfScore_app.models.player import Player

class Score(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    date = models.DateField()
    score = models.IntegerField()
