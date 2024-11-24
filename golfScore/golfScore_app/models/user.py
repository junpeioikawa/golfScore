from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# class UserManager(BaseUserManager):
#     def _create_user(self, email, account_id, password, **extra_fields):
#         email = self.normalize_email(email) # emailを正規化
#         user = self.model(email = email, account_id = account_id, **extra_fields)
#         user.set_password(password) # パスワードを暗号化
#         user.save(using = self._db) # ユーザーをDBに保存
        
#         return user
    
#     def create_user(self, email, account_id, password = None, **extra_fields):
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
        
#         return self._create_user(
#             email = email,
#             account_id = account_id,
#             password = password,
#             **extra_fields,
#         )
        
#     def create_superuser(self, email, account_id, password, **extra_fields):
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
        
#         return self._create_user(
#             email = email,
#             account_id = account_id,
#             password = password,
#             **extra_fields,
#         )

class CustomUser(AbstractUser):
    """ 拡張ユーザーモデル """
    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'
    
    age = models.IntegerField('年齢', blank=True, null=True)
    