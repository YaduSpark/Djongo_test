from django.contrib import admin

from djongo_app.models import Product, ProductCategory, ProductManufacturer

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(ProductManufacturer)
admin.site.register(Product)