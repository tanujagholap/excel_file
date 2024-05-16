from django.db import models


class Product(models.Model):
    pro_id = models.IntegerField()
    name = models.CharField(max_length=40)
    price = models.FloatField()
    quantity = models.IntegerField()
