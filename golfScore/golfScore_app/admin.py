from django.contrib import admin

# Register your models here.
from .models import Player, Score

admin.site.register(Player)
admin.site.register(Score)