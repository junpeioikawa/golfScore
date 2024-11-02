from django.db import models
from django.utils import timezone

class GolfHouseMaster(models.Model):
    house_id = models.AutoField(primary_key=True, verbose_name='ゴルフ場ID')  # ゴルフ場ID
    house_name = models.CharField(max_length=255, null=False, blank=False, verbose_name='ゴルフ場名')  # ゴルフ場名
    house_zipcode = models.CharField(max_length=8, null=False, blank=False, verbose_name='郵便番号')  # 郵便番号
    house_prefecture = models.CharField(max_length=40, null=False, blank=False, verbose_name='都道府県')  # 都道府県
    house_city = models.CharField(max_length=100, null=False, blank=False, verbose_name='市町村区')  # 市町村区
    house_address = models.CharField(max_length=255, null=False, blank=False, verbose_name='住所')  # 住所
    house_phone_number = models.CharField(max_length=11, null=False, blank=False, verbose_name='電話番号')  # 電話番号
    create_at = models.DateTimeField(default=timezone.now)  # 登録日
    update_at = models.DateTimeField(auto_now=True)  # 更新日
    
    def __str__(self):
        return self.house_name
