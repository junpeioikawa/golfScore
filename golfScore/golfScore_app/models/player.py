import uuid
from django.db import models
from django.utils import timezone

class Player(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)  # ユーザID
    name = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100,null=True, blank=True)
    create_at = models.DateTimeField(default=timezone.now)  # 登録日
    update_at = models.DateTimeField(auto_now=True)  # 更新日


    def __str__(self):
        return self.name
