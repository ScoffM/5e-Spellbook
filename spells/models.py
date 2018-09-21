from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator


class Spell(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    school = models.CharField(max_length=255)
    level = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(9)])
    ritual = models.BooleanField()
    casting_time = models.CharField(max_length=255)
    range = models.IntegerField()
    verbal = models.BooleanField()
    somatic = models.BooleanField()
    material = models.CharField(max_length=255)
    concentration = models.BooleanField()
    duration = models.CharField(max_length=255)
    description = models.TextField()
    class_list = models.CharField(max_length=255)

    def __str__(self):
        return self.name
