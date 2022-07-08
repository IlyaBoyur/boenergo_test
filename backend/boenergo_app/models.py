from django.core import validators
from django.db import models

# Item colors
BLUE = 0x1279FF
GREEN = 0x1C811C
RED = 0xFF1245


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
