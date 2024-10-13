from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, validators=[validate_email])

    def __str__(self):
        return self.username
