import uuid
from django.db import models
from django.utils import timezone


# Create your models here.
class Player(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)  # ユーザID
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(default=timezone.now)  # 登録日
    update_at = models.DateTimeField(auto_now=True)  # 更新日


    def __str__(self):
        return self.name

class Score(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    date = models.DateField()
    score = models.IntegerField()
    

    def __str__(self):
        return f"{self.player.name} - {self.score} ({self.date})"

# class CourseMaster(models.Model):
#     course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)  # コースID
#     course_name = models.CharField(max_length=255, null=True, blank=True)  # ゴルフ場名
#     course_zipcode = models.CharField(max_length=8, null=True, blank=False)  # 郵便番号
#     course_prefecture = models.CharField(max_length=40, null=False, blank=False)  # 都道府県
#     course_city = models.CharField(max_length=100, null=False, blank=False)  # 市町村区
#     course_address = models.CharField(max_length=255, null=False, blank=False)  # 住所
#     course_phone_number = models.CharField(max_length=11, null=False, blank=False)  # 電話番号
#     create_at = models.DateTimeField(alse)  # 登録日
#     update_at = models.DateTimeField(blank=False, null=False)  # 更新日






# 2024/10/23 hayashida start
class GolfHouseMaster(models.Model):
    house_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)  # ゴルフ場ID
    house_name = models.CharField(max_length=255, null=False, blank=False)  # ゴルフ場名
    house_zipcode = models.CharField(max_length=8, null=False, blank=False)  # 郵便番号
    house_prefecture = models.CharField(max_length=40, null=False, blank=False)  # 都道府県
    house_city = models.CharField(max_length=100, null=False, blank=False)  # 市町村区
    house_address = models.CharField(max_length=255, null=False, blank=False)  # 住所
    house_phone_number = models.CharField(max_length=11, null=False, blank=False)  # 電話番号
    create_at = models.DateTimeField(default=timezone.now)  # 登録日
    update_at = models.DateTimeField(auto_now=True)  # 更新日
    
class CourseMaster(models.Model):
    house_id = models.ForeignKey(GolfHouseMaster, on_delete=models.CASCADE)
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)  # コースID
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
    hole_1 = models.IntegerField(blank=True, null=True)
    hole_2 = models.IntegerField(blank=True, null=True)
    hole_3 = models.IntegerField(blank=True, null=True)
    hole_4 = models.IntegerField(blank=True, null=True)
    hole_5 = models.IntegerField(blank=True, null=True)
    hole_6 = models.IntegerField(blank=True, null=True)
    hole_7 = models.IntegerField(blank=True, null=True)
    hole_8 = models.IntegerField(blank=True, null=True)
    hole_9 = models.IntegerField(blank=True, null=True)
    hole_10 = models.IntegerField(blank=True, null=True)
    hole_11 = models.IntegerField(blank=True, null=True)
    hole_12 = models.IntegerField(blank=True, null=True)
    hole_13 = models.IntegerField(blank=True, null=True)
    hole_14 = models.IntegerField(blank=True, null=True)
    hole_15 = models.IntegerField(blank=True, null=True)
    hole_16 = models.IntegerField(blank=True, null=True)
    hole_17 = models.IntegerField(blank=True, null=True)
    hole_18 = models.IntegerField(blank=True, null=True)
    hole_19 = models.IntegerField(blank=True, null=True)
    hole_20 = models.IntegerField(blank=True, null=True)
    hole_21 = models.IntegerField(blank=True, null=True)
    hole_22 = models.IntegerField(blank=True, null=True)
    hole_23 = models.IntegerField(blank=True, null=True)
    hole_24 = models.IntegerField(blank=True, null=True)
    hole_25 = models.IntegerField(blank=True, null=True)
    hole_26 = models.IntegerField(blank=True, null=True)
    hole_27 = models.IntegerField(blank=True, null=True)
    # ハンディキャップ1-27
    handicap_1 = models.IntegerField( blank=True, null=True)
    handicap_2 = models.IntegerField( blank=True, null=True)
    handicap_3 = models.IntegerField( blank=True, null=True)
    handicap_4 = models.IntegerField( blank=True, null=True)
    handicap_5 = models.IntegerField( blank=True, null=True)
    handicap_6 = models.IntegerField( blank=True, null=True)
    handicap_7 = models.IntegerField( blank=True, null=True)
    handicap_8 = models.IntegerField( blank=True, null=True)
    handicap_9 = models.IntegerField( blank=True, null=True)
    handicap_10 = models.IntegerField( blank=True, null=True)
    handicap_11 = models.IntegerField( blank=True, null=True)
    handicap_12 = models.IntegerField( blank=True, null=True)
    handicap_13 = models.IntegerField( blank=True, null=True)
    handicap_14 = models.IntegerField( blank=True, null=True)
    handicap_15 = models.IntegerField( blank=True, null=True)
    handicap_16 = models.IntegerField( blank=True, null=True)
    handicap_17 = models.IntegerField( blank=True, null=True)
    handicap_18 = models.IntegerField( blank=True, null=True)
    handicap_19 = models.IntegerField( blank=True, null=True)
    handicap_20 = models.IntegerField( blank=True, null=True)
    handicap_21 = models.IntegerField( blank=True, null=True)
    handicap_22 = models.IntegerField( blank=True, null=True)
    handicap_23 = models.IntegerField( blank=True, null=True)
    handicap_24 = models.IntegerField( blank=True, null=True)
    handicap_25 = models.IntegerField( blank=True, null=True)
    handicap_26 = models.IntegerField( blank=True, null=True)
    handicap_27 = models.IntegerField( blank=True, null=True)
    # パー1-27
    par_1 = models.IntegerField( blank=True, null=True)
    par_2 = models.IntegerField( blank=True, null=True)
    par_3 = models.IntegerField( blank=True, null=True)
    par_4 = models.IntegerField( blank=True, null=True)
    par_5 = models.IntegerField( blank=True, null=True)
    par_6 = models.IntegerField( blank=True, null=True)
    par_7 = models.IntegerField( blank=True, null=True)
    par_8 = models.IntegerField( blank=True, null=True)
    par_9 = models.IntegerField( blank=True, null=True)
    par_10 = models.IntegerField( blank=True, null=True)
    par_11 = models.IntegerField( blank=True, null=True)
    par_12 = models.IntegerField( blank=True, null=True)
    par_13 = models.IntegerField( blank=True, null=True)
    par_14 = models.IntegerField( blank=True, null=True)
    par_15 = models.IntegerField( blank=True, null=True)
    par_16 = models.IntegerField( blank=True, null=True)
    par_17 = models.IntegerField( blank=True, null=True)
    par_18 = models.IntegerField( blank=True, null=True)
    par_19 = models.IntegerField( blank=True, null=True)
    par_20 = models.IntegerField( blank=True, null=True)
    par_21 = models.IntegerField( blank=True, null=True)
    par_22 = models.IntegerField( blank=True, null=True)
    par_23 = models.IntegerField( blank=True, null=True)
    par_24 = models.IntegerField( blank=True, null=True)
    par_25 = models.IntegerField( blank=True, null=True)
    par_26 = models.IntegerField( blank=True, null=True)
    par_27 = models.IntegerField( blank=True, null=True)
    create_at = models.DateTimeField(default=timezone.now)  # 登録日
    update_at = models.DateTimeField(auto_now=True)  # 更新日



# 2024/10/23 oikawa_end

# Git テスト2