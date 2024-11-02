from django.db import models
from django.utils import timezone
from golfScore_app.models.golfHouseMaster import GolfHouseMaster
from golfScore_app.models.courseMaster import CourseMaster

class TeeingAreaMaster(models.Model):
    teeing_area_id = models.AutoField(primary_key=True)
    house_id = models.ForeignKey(GolfHouseMaster, on_delete=models.CASCADE)
    course_id = models.ForeignKey(CourseMaster, on_delete=models.CASCADE)
    teeing_area_name = models.CharField(max_length=255, null=False, blank=False, verbose_name='ティーイングエリア名')
    yard_1 = models.IntegerField( blank=True, null=True)
    yard_2 = models.IntegerField( blank=True, null=True)
    yard_3 = models.IntegerField( blank=True, null=True)
    yard_4 = models.IntegerField( blank=True, null=True)
    yard_5 = models.IntegerField( blank=True, null=True)
    yard_6 = models.IntegerField( blank=True, null=True)
    yard_7 = models.IntegerField( blank=True, null=True)
    yard_8 = models.IntegerField( blank=True, null=True)
    yard_9 = models.IntegerField( blank=True, null=True)
    create_at = models.DateTimeField(default=timezone.now)  # 登録日
    update_at = models.DateTimeField(auto_now=True)  # 更新日
    
    def __str__(self):
        return self.teeing_area_name
