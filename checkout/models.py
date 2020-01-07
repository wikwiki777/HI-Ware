from django.db import models
from products.models import Product


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    street_address1 = models.CharField(max_length=50, blank=False)
    street_address2 = models.CharField(max_length=50, blank=False)
    postcode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=50, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.full_name, self.date)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.quantity, self.product.brand,
                                        self.product.model, self.product.price)
