from django.contrib import admin
from products import models


class BaseProductsAdmin(admin.ModelAdmin):
    list_display = ("category", "created_date")


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("baseproduct", "brand", "model", "price", "created_date")


admin.site.register(models.Category)
admin.site.register(models.BaseProduct, BaseProductsAdmin)
admin.site.register(models.Product, ProductsAdmin)
