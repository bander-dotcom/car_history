from django.db import models

class Car(models.Model):
    vin =models.CharField(Max_length=50, unique=True)
    make = models.CharField(Max_length=100, blank=True)
    model = models.CharField(Max_length=100, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    mileage = models.PositiveIntegerField(null=True, blank=True)
    color = models.CharField(Max_length=50, blank=True)
    last_service = models.DataField(null=True, blank=True)
    created_at = models.DataField(auto_now_add=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.vin})"
