from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Users(models.Model):

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(null=False, max_length=30)
    last_name = models.CharField(null=False, max_length=30)
    phone_regex = RegexValidator(regex=r'^01[1|0|2|5][0-9]{8}$', message='phone must be an egyptian phone number...')
    phone = models.CharField(null=False, validators=[phone_regex], max_length=14)
    email = models.EmailField(null=False, max_length=250)
    password = models.CharField(null=False, max_length=30)

