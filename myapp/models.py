from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MinValueValidator(5),MaxValueValidator(100)])

