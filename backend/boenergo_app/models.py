items = None

BLUE = 'rgb(18, 121, 255)'
GREEN = 'rgb(28, 129, 28)'
RED = 'rgb(255, 18, 69)'

from django.core import validators
from django.db import models

class Item(models.Model):
    number = models.PositiveSmallIntegerField(
        'Порядковый номер'
    )
    is_revealed = models.BooleanField(
        'Раскрыт ли реальный цвет'
    )
    color_guess = models.PositiveIntegerField(
        'Предполагаемый цвет в HEX',
        validators=(
            validators.MaxValueValidator(0xFFFFFF,
                                         'Превышен максимум для цвета'),
        ),
    )
    color_actual = models.PositiveIntegerField(
        'Реальный цвет в HEX',
        validators=(
            validators.MaxValueValidator(0xFFFFFF,
                                         'Превышен максимум для цвета'),
        ),
    )
