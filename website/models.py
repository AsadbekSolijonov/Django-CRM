from django.db import models
from django.db.models import Model, IntegerField, CharField
from .validators import even_number_validate, odd_number_validate, phone_number_validate


# Create your models here.
class MyModel(Model):
    even_field = IntegerField(validators=[even_number_validate])
    odd_filed = IntegerField(validators=[odd_number_validate])
    phone = CharField(max_length=11, validators=[phone_number_validate])

