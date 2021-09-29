from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Vendor(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Model(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    password_type = models.IntegerField(default=2)
    password = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    model = ChainedForeignKey(Model, chained_field="vendor", chained_model_field="vendor", show_all=False,
                              auto_choose=True, sort=True, on_delete=models.CASCADE)
