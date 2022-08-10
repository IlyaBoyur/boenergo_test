import random
from cmath import sqrt as sqrt_imaginary
from datetime import datetime
from math import sqrt
from typing import List, Tuple, Union

from django.core.cache import cache
from django.shortcuts import get_object_or_404

from .models import BLUE, GREEN, RED, Item

# How many items overall
ITEMS_COUNT = 100
# How many times more blues than greens
TIMES_BLUES_MORE_GREENS = 5


def calculate_square_roots(a: float, b: float, c: float) -> Union[
    Tuple[float, float],
    Tuple[complex, complex]
]:
    descriminant = b * b - 4 * a * c
    descriminant_sqrt = (
        sqrt_imaginary(descriminant)
        if descriminant < 0
        else sqrt(descriminant)
    )
    return tuple([((-b + descriminant_sqrt) / 2 / a),
                  ((-b - descriminant_sqrt) / 2 / a)])


def generate_random_number(min: int, max: int) -> int:
    """Generate a random number

    min - lowest posible value
    max - highest posible value
    """
    random.seed(datetime.utcnow())
    return random.randint(min, max)


def generate_random_places(min: int, max: int, count: int) -> List[int]:
    """Generate a list of random non-repeating indices

    min - lowest index value
    max - highest index value
    count - number of indices
    """
    random.seed(datetime.utcnow())
    return random.sample(range(min, max + 1), count)


def get_items():
    """Return items or create new"""
    items = Item.objects.all().order_by('number')[:ITEMS_COUNT]
    if not items:
        *_, items = create_items()
    return items


def get_items_counts() -> Tuple[int, int, int]:
    """Return item counts or create new"""
    if cache.get('items_counts') is not None:
        return cache.get('items_counts')
    blue, green, red = 0, 0, 0
    for item in get_items():
        if item.color_actual == RED:
            red += 1
        if item.color_actual == GREEN:
            green += 1
        if item.color_actual == BLUE:
            blue += 1
    cache.set('items_counts', (blue, green, red,))
    return blue, green, red


def update_items(index: int) -> None:
    item = get_object_or_404(Item, number=index)
    item.is_revealed = True
    item.save()


def randomize_items() -> None:
    """Create and shuffle new items"""
    Item.objects.all().delete()
    blue, green, red, *_ = create_items()
    cache.set('items_counts', (blue, green, red,))


def create_items() -> Tuple[int, int, int, List[Item]]:
    """Create and shuffle new items"""
    blue, green, red = randomize_colors(all=ITEMS_COUNT)
    places = generate_random_places(0, ITEMS_COUNT-1, ITEMS_COUNT)

    blues = [
        Item(number=places.pop(),
             is_revealed=False,
             color_guess=BLUE,
             color_actual=BLUE)
        for _ in range(blue)
    ]
    greens = [
        Item(number=places.pop(),
             is_revealed=False,
             color_guess=GREEN,
             color_actual=GREEN)
        for _ in range(green)
    ]
    reds = [
        Item(number=places.pop(),
             is_revealed=False,
             color_guess=RED,
             color_actual=RED)
        for _ in range(red)
    ]
    return blue, green, red, Item.objects.bulk_create([*blues, *greens, *reds])


def randomize_colors(times: int = TIMES_BLUES_MORE_GREENS,
                     all: int = ITEMS_COUNT):
    """
    1) Find out red_min and red_max:
    red_min = 1
    times * (red_max + 1) + red_max + 1 + red_max = all

    2) Generate red
    red = red_min .. red_max

    3) Calculate green and blue:
    times * green + green + red <= all
    blue = all - green - red
    """
    red_max = (all - (times + 1)) // (times + 2)
    red = generate_random_number(1, red_max)
    green = (all - red) // (times + 1)
    blue = all - green - red
    return blue, green, red
