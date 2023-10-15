from django.db import models
from django.contrib.auth.models import (
  AbstractBaseUser,
  PermissionsMixin
)

class Users(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=255)
  age = models.PositiveIntegerField()
  email = models.EmailField(max_length=255, unique=True)
  is_active = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  picture = models.FileField(null=True, upload_to='picture/')

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  class Meta:
    db_table = 'users'

class UserActivateTokens(models.Model):
  token = models.UUIDField(db_index=True)
  expired_at = models.DateTimeField()
  user = models.ForeignKey(
    'Users', on_delete=models.CASCADE
  )

  class Meta:
    db_table = 'user_activate_tokens'