from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BaseProduct(models.Model):
    description = models.TextField(max_length=500)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
