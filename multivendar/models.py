from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    vendor_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_logo = models.ImageField(
        upload_to='logos/',
        blank=True,
        null=True
    )
    def __str__(self):
        return self.vendor_name


class Product(models.Model):
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE
    )
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    product_image = models.ImageField(
        upload_to='products/'
    )

    def __str__(self):
        return self.product_name