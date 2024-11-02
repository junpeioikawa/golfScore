from django.db import models
from django.utils import timezone
from golfScore_app.models.golfHouseMaster import GolfHouseMaster

class CourseMaster(models.Model):
    house_id = models.ForeignKey(GolfHouseMaster, on_delete=models.CASCADE)
    course_id = models.AutoField(primary_key=True)  # コースID
    course_name = models.CharField(max_length=255, null=False, blank=False)  # コース名
    hole_number_1 = models.IntegerField( null=False, blank=False)
    hole_number_2 = models.IntegerField( null=False, blank=False)
    hole_number_3 = models.IntegerField( null=False, blank=False)
    hole_number_4 = models.IntegerField( null=False, blank=False)
    hole_number_5 = models.IntegerField( null=False, blank=False)
    hole_number_6 = models.IntegerField( null=False, blank=False)
    hole_number_7 = models.IntegerField( null=False, blank=False)
    hole_number_8 = models.IntegerField( null=False, blank=False)
    hole_number_9 = models.IntegerField( null=False, blank=False)
    par_1 = models.IntegerField( null=False, blank=False)
    par_2 = models.IntegerField( null=False, blank=False)
    par_3 = models.IntegerField( null=False, blank=False)
    par_4 = models.IntegerField( null=False, blank=False)
    par_5 = models.IntegerField( null=False, blank=False)
    par_6 = models.IntegerField( null=False, blank=False)
    par_7 = models.IntegerField( null=False, blank=False)
    par_8 = models.IntegerField( null=False, blank=False)
    par_9 = models.IntegerField( null=False, blank=False)
    handicap_1 = models.IntegerField( null=False, blank=False)
    handicap_2 = models.IntegerField( null=False, blank=False)
    handicap_3 = models.IntegerField( null=False, blank=False)
    handicap_4 = models.IntegerField( null=False, blank=False)
    handicap_5 = models.IntegerField( null=False, blank=False)
    handicap_6 = models.IntegerField( null=False, blank=False)
    handicap_7 = models.IntegerField( null=False, blank=False)
    handicap_8 = models.IntegerField( null=False, blank=False)
    handicap_9 = models.IntegerField( null=False, blank=False)
    create_at = models.DateTimeField(default=timezone.now)  # 登録日
    update_at = models.DateTimeField(auto_now=True)  # 更新日
    
    def __str__(self):
        return f"{self.house_id.house_name} - {self.course_name}"