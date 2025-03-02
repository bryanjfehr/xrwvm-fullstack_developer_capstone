from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Other fields as needed
    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
        ("PICKUP", "Pickup"),
    ]
    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default="SUV"
    )
    year = models.IntegerField(
        default=2025,
        validators=[
            MaxValueValidator(2025),
            MinValueValidator(1950),
        ]
    )

    def __str__(self):
        return self.name  # Return the name as the string representation