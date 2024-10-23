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

    def __str__(self):
        return self.name
