from django.contrib import admin

# Register your models here.

from.models import Vendor
from.models import Product

admin.site.register(Vendor)
admin.site.register(Product)
