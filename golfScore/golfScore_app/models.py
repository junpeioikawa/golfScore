import uuid
from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)  # ユーザID
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(blank=False, null=False)  # 登録日
    update_at = models.DateTimeField(blank=False, null=False)  # 更新日


    def __str__(self):
        return self.name

class Score(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
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

# 2024/10/23 oikawa_str
class Round(models.Model):
    round_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)  # ラウンドID
    course_id = models.ForeignKey(CourseMaster,on_delete=models.PROTECT)  # コースID
    play_date = models.DateTimeField(blank=False, null=False)  # プレイ日
    weather = models.CharField(verbose_name="choice", max_length=255,blank=False, null=False) # 天気
    wind =  models.CharField(verbose_name="choice", max_length=255,blank=False, null=False) # 風
    first_round = models.CharField(verbose_name="choice", max_length=255,blank=False, null=False)# 前半
    second_round = models.CharField(verbose_name="choice", max_length=255,blank=False, null=False)# 後半
    ex_round = models.CharField(verbose_name="choice", max_length=255, blank=True, null=True) # 追加ラウンド
    teeing_area = models.CharField(verbose_name="choice", max_length=255, blank=True, null=True) # ティー
    green = models.CharField(verbose_name="choice", max_length=255, blank=True, null=True) # グリーン
    # ホール1-27
    hole_1 = models.IntegerField(blank=False, null=False)
    hole_2 = models.IntegerField(blank=False, null=False)
    hole_3 = models.IntegerField(blank=False, null=False)
    hole_4 = models.IntegerField(blank=False, null=False)
    hole_5 = models.IntegerField(blank=False, null=False)
    hole_6 = models.IntegerField(blank=False, null=False)
    hole_7 = models.IntegerField(blank=False, null=False)
    hole_8 = models.IntegerField(blank=False, null=False)
    hole_9 = models.IntegerField(blank=False, null=False)
    hole_10 = models.IntegerField(blank=False, null=False)
    hole_11 = models.IntegerField(blank=False, null=False)
    hole_12 = models.IntegerField(blank=False, null=False)
    hole_13 = models.IntegerField(blank=False, null=False)
    hole_14 = models.IntegerField(blank=False, null=False)
    hole_15 = models.IntegerField(blank=False, null=False)
    hole_16 = models.IntegerField(blank=False, null=False)
    hole_17 = models.IntegerField(blank=False, null=False)
    hole_18 = models.IntegerField(blank=False, null=False)
    hole_19 = models.IntegerField(blank=False, null=False)
    hole_20 = models.IntegerField(blank=False, null=False)
    hole_21 = models.IntegerField(blank=False, null=False)
    hole_22 = models.IntegerField(blank=False, null=False)
    hole_23 = models.IntegerField(blank=False, null=False)
    hole_24 = models.IntegerField(blank=False, null=False)
    hole_25 = models.IntegerField(blank=False, null=False)
    hole_26 = models.IntegerField(blank=False, null=False)
    hole_27 = models.IntegerField(blank=False, null=False)
    # ハンディキャップ1-27
    handicap_1 = models.IntegerField(blank=False, null=False)
    handicap_2 = models.IntegerField(blank=False, null=False)
    handicap_3 = models.IntegerField(blank=False, null=False)
    handicap_4 = models.IntegerField(blank=False, null=False)
    handicap_5 = models.IntegerField(blank=False, null=False)
    handicap_6 = models.IntegerField(blank=False, null=False)
    handicap_7 = models.IntegerField(blank=False, null=False)
    handicap_8 = models.IntegerField(blank=False, null=False)
    handicap_9 = models.IntegerField(blank=False, null=False)
    handicap_10 = models.IntegerField(blank=False, null=False)
    handicap_11 = models.IntegerField(blank=False, null=False)
    handicap_12 = models.IntegerField(blank=False, null=False)
    handicap_13 = models.IntegerField(blank=False, null=False)
    handicap_14 = models.IntegerField(blank=False, null=False)
    handicap_15 = models.IntegerField(blank=False, null=False)
    handicap_16 = models.IntegerField(blank=False, null=False)
    handicap_17 = models.IntegerField(blank=False, null=False)
    handicap_18 = models.IntegerField(blank=False, null=False)
    handicap_19 = models.IntegerField(blank=False, null=False)
    handicap_20 = models.IntegerField(blank=False, null=False)
    handicap_21 = models.IntegerField(blank=False, null=False)
    handicap_22 = models.IntegerField(blank=False, null=False)
    handicap_23 = models.IntegerField(blank=False, null=False)
    handicap_24 = models.IntegerField(blank=False, null=False)
    handicap_25 = models.IntegerField(blank=False, null=False)
    handicap_26 = models.IntegerField(blank=False, null=False)
    handicap_27 = models.IntegerField(blank=False, null=False)
    # パー1-27
    par_1 = models.IntegerField(blank=False, null=False)
    par_2 = models.IntegerField(blank=False, null=False)
    par_3 = models.IntegerField(blank=False, null=False)
    par_4 = models.IntegerField(blank=False, null=False)
    par_5 = models.IntegerField(blank=False, null=False)
    par_6 = models.IntegerField(blank=False, null=False)
    par_7 = models.IntegerField(blank=False, null=False)
    par_8 = models.IntegerField(blank=False, null=False)
    par_9 = models.IntegerField(blank=False, null=False)
    par_10 = models.IntegerField(blank=False, null=False)
    par_11 = models.IntegerField(blank=False, null=False)
    par_12 = models.IntegerField(blank=False, null=False)
    par_13 = models.IntegerField(blank=False, null=False)
    par_14 = models.IntegerField(blank=False, null=False)
    par_15 = models.IntegerField(blank=False, null=False)
    par_16 = models.IntegerField(blank=False, null=False)
    par_17 = models.IntegerField(blank=False, null=False)
    par_18 = models.IntegerField(blank=False, null=False)
    par_19 = models.IntegerField(blank=False, null=False)
    par_20 = models.IntegerField(blank=False, null=False)
    par_21 = models.IntegerField(blank=False, null=False)
    par_22 = models.IntegerField(blank=False, null=False)
    par_23 = models.IntegerField(blank=False, null=False)
    par_24 = models.IntegerField(blank=False, null=False)
    par_25 = models.IntegerField(blank=False, null=False)
    par_26 = models.IntegerField(blank=False, null=False)
    par_27 = models.IntegerField(blank=False, null=False)



# 2024/10/23 oikawa_end