from django.db import models
from django.utils import timezone
from golfScore_app.models import GolfHouseMaster, CourseMaster, TeeingAreaMaster


class TeeingAreaYardMaster(models.Model):
    house_id = models.ForeignKey(GolfHouseMaster, on_delete=models.CASCADE)
    course_id = models.ForeignKey(CourseMaster, on_delete=models.CASCADE)
    teeing_area_id = models.ForeignKey(TeeingAreaMaster, on_delete=models.CASCADE)
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
        return f"{self.house_id.house_name} - {self.course_id.course_name} - {self.teeing_area_id.teeing_area_name}"
