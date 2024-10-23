import uuid
from django.db import models
from django.utils import timezone


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Score(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    date = models.DateField()
    score = models.IntegerField()

    def __str__(self):
        return f"{self.player.name} - {self.score} ({self.date})"

class CourseMaster(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)  # コースID
    course_name = models.CharField(max_length=255, null=False, blank=False)  # ゴルフ場名
    course_zipcode = models.CharField(max_length=8, null=False, blank=False)  # 郵便番号
    course_prefecture = models.CharField(max_length=40, null=False, blank=False)  # 都道府県
    course_city = models.CharField(max_length=100, null=False, blank=False)  # 市町村区
    course_address = models.CharField(max_length=255, null=False, blank=False)  # 住所
    course_phone_number = models.CharField(max_length=11, null=False, blank=False)  # 電話番号
    create_at = models.DateTimeField(blank=False, null=False)  # 登録日
    update_at = models.DateTimeField(blank=False, null=False)  # 更新日






# 2024/10/23 hayashida start
class GolfHouseMaster(models.Model):
    house_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)  # ゴルフ場ID
    house_name = models.CharField(max_length=255, null=False, blank=False)  # ゴルフ場名
    house_zipcode = models.CharField(max_length=8, null=False, blank=False)  # 郵便番号
    house_prefecture = models.CharField(max_length=40, null=False, blank=False)  # 都道府県
    house_city = models.CharField(max_length=100, null=False, blank=False)  # 市町村区
    house_address = models.CharField(max_length=255, null=False, blank=False)  # 住所
    house_phone_number = models.CharField(max_length=11, null=False, blank=False)  # 電話番号
    create_at = models.DateTimeField(blank=False, null=False)  # 登録日
    update_at = models.DateTimeField(blank=False, null=False)  # 更新日
    
class CorseMaster(models.Model):
    house_id = models.ForeignKey(GolfHouseMaster, on_delete=models.CASCADE)
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)  # コースID
    course_name = models.CharField(max_length=255, null=False, blank=False)  # コース名
    hole_number_1 = models.IntegerField(max_length=2, null=False, blank=False)
    hole_number_2 = models.IntegerField(max_length=2, null=False, blank=False)
    hole_number_3 = models.IntegerField(max_length=2, null=False, blank=False)
    hole_number_4 = models.IntegerField(max_length=2, null=False, blank=False)
    hole_number_5 = models.IntegerField(max_length=2, null=False, blank=False)
    hole_number_6 = models.IntegerField(max_length=2, null=False, blank=False)
    hole_number_7 = models.IntegerField(max_length=2, null=False, blank=False)
    hole_number_8 = models.IntegerField(max_length=2, null=False, blank=False)
    hole_number_9 = models.IntegerField(max_length=2, null=False, blank=False)
    par_1 = models.IntegerField(max_length=2, null=False, blank=False)
    par_2 = models.IntegerField(max_length=2, null=False, blank=False)
    par_3 = models.IntegerField(max_length=2, null=False, blank=False)
    par_4 = models.IntegerField(max_length=2, null=False, blank=False)
    par_5 = models.IntegerField(max_length=2, null=False, blank=False)
    par_6 = models.IntegerField(max_length=2, null=False, blank=False)
    par_7 = models.IntegerField(max_length=2, null=False, blank=False)
    par_8 = models.IntegerField(max_length=2, null=False, blank=False)
    par_9 = models.IntegerField(max_length=2, null=False, blank=False)
    handicap_1 = models.IntegerField(max_length=2, null=False, blank=False)
    handicap_2 = models.IntegerField(max_length=2, null=False, blank=False)
    handicap_3 = models.IntegerField(max_length=2, null=False, blank=False)
    handicap_4 = models.IntegerField(max_length=2, null=False, blank=False)
    handicap_5 = models.IntegerField(max_length=2, null=False, blank=False)
    handicap_6 = models.IntegerField(max_length=2, null=False, blank=False)
    handicap_7 = models.IntegerField(max_length=2, null=False, blank=False)
    handicap_8 = models.IntegerField(max_length=2, null=False, blank=False)
    handicap_9 = models.IntegerField(max_length=2, null=False, blank=False)
    
# 2024/10/23 hayashida end