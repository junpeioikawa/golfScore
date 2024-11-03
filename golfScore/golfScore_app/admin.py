from django.contrib import admin

# Register your models here.
from .models import Player, Score, GolfHouseMaster, CourseMaster, Round, TeeingAreaMaster, TeeingAreaYardMaster

admin.site.register(Player)
admin.site.register(Score)
admin.site.register(GolfHouseMaster)
admin.site.register(CourseMaster)
admin.site.register(Round)
admin.site.register(TeeingAreaMaster)
admin.site.register(TeeingAreaYardMaster)