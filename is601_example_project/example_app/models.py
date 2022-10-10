from django.db import models

class BakedGood(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    good_type = models.CharField(
        max_length=2,
        choices=[("BR", "Bread"), ("CA", "Cake"), ("CO", "Cookie"), ("PR", "Pretzel")],
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    recipe = models.TextField()
