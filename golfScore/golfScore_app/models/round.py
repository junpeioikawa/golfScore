import uuid
from django.db import models
from django.utils import timezone
from golfScore_app.models.golfHouseMaster import GolfHouseMaster
#golf_score_app
class Round(models.Model):
    round_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)  # ラウンドID
    house_id = models.ForeignKey(GolfHouseMaster,on_delete=models.PROTECT)  # ハウスID
    play_date = models.DateField(blank=False, null=False)  # プレイ日
    weather = models.CharField( max_length=255,blank=False, null=False) # 天気
    wind =  models.CharField( max_length=255,blank=False, null=False) # 風
    first_round = models.CharField( max_length=255,blank=False, null=False)# 前半
    second_round = models.CharField( max_length=255,blank=False, null=False)# 後半
    ex_round = models.CharField( max_length=255, blank=True, null=True) # 追加ラウンド
    teeing_area = models.CharField( max_length=255, blank=True, null=True) # ティー
    green = models.CharField( max_length=255, blank=True, null=True) # グリーン
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

