from django.db import models
from django.contrib.postgres.fields import JSONField


class Category(models.Model):
    name = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BaseProduct(models.Model):
    description = models.TextField(max_length=500)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category.name


class Product(models.Model):
    baseproduct = models.ForeignKey(BaseProduct, on_delete=models.CASCADE)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    specifications = JSONField()
    images = models.ImageField()
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.brand, self.model)
