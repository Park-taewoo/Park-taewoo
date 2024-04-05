from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# User class 작성
class User(AbstractUser):
    # 상속은 받았지만 내용은 작성하지 않아요
    # 필요할 때 작성하면 됩니다. 
    pass
