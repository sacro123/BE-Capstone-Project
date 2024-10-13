from django.db import models
from django.core.validators import MinValueValidator, validate_email
from django.forms import ValidationError
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    category = models.CharField(max_length=100)
    stock_quantity = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    image_url = models.URLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products', null=True, blank=True)


    def __str__(self):
        return self.name

    def reduce_stock(self, quantity):
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            self.save()
        else:
            raise ValidationError(f"Not enough stock. Available: {self.stock_quantity}")

