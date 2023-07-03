from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.

class User_table(models.Model):
    user_id = models.IntegerField(validators=[
            MaxLengthValidator(10),
            MinLengthValidator(0)
        ])
    name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[
            MaxLengthValidator(3),
            MinLengthValidator(1)
        ])
    phone = models.CharField(null=True)