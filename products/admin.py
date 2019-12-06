from django.contrib import admin
from products import models


class BaseProductsAdmin(admin.ModelAdmin):
    list_display = ("category", "created_date")


admin.site.register(models.Category)
admin.site.register(models.BaseProduct, BaseProductsAdmin)
