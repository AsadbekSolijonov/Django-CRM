from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


def even_number_validate(value):
    if not isinstance(value, int):
        raise ValidationError(f"{value} soni butun son emas. Iltimos butun son kiriting.")
    if value % 2 != 0:
        raise ValidationError(f"{value} soni juft son emas.")


def odd_number_validate(value):
    if value % 2 != 1:
        raise ValidationError(f"{value} soni toq son emas.")


def phone_number_validate(value):
    import re
    phone_number_regex = r'^(?:\+998|8)?\s?\d{2}\s?\d{3}\s?\d{4}$'
    if not re.match(phone_number_regex, value):
        raise ValidationError(_("%(value)s isn't a valid phone number."), code='invalid', params={'value': value})


class CustomSeperatedIntegerField(models.Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return "VARCHAR"
