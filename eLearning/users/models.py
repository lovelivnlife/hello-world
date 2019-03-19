from django.db import models
from django.contrib.auth.models import AbstractUser
from users.choices import *

class CustomUser(AbstractUser):
    # add additional fields in here
    userType = models.IntegerField("User role", choices=USER_TYPES, default=1)

    def __int__(self):
        return self.userType

    def __str__(self):
        return self.email

    def __str__(self):
        return self.first_name

    def __str__(self):
        return self.last_name
