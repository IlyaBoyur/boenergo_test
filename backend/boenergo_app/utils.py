import random

from cmath import sqrt as sqrt_imaginary
from datetime import datetime
from math import sqrt
from typing import Dict, List, Tuple, Union

from .models import BLUE, GREEN, RED, items, items_counts

# How many items overall
ITEMS_COUNT = 100
# How many times more blues than greens
TIMES_BLUES_MORE_GREENS = 5


Item = Dict[str, Union[int, bool, str]]


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


def get_items() -> List[Item]:
    """Return items or create new"""
    global items, items_counts
    if not items:
        blue, green, red, items = create_items()
        items_counts = blue, green, red
    return items


def get_items_counts() -> Tuple[int, int, int]:
    """Return item counts or create new"""
    global items, items_counts
    if not items_counts:
        blue, green, red, items = create_items()
        items_counts = blue, green, red
    return items_counts


def update_items(index: int) -> None:
    get_items()[index]['is_revealed'] = True


def randomize_items() -> None:
    """Create and shuffle new items"""
    global items, items_counts
    blue, green, red, items = create_items()
    items_counts = blue, green, red


def create_items() -> Tuple[int, int, int, List[Item]]:
    """Create and shuffle new items"""
    new_items = list(
        {'id': i, 'is_revealed': False, 'guess': BLUE, 'actual': BLUE, }
        for i in range(ITEMS_COUNT)
    )

    blue, green, red = randomize_colors()
    places = generate_random_places(0, ITEMS_COUNT-1, ITEMS_COUNT)
    for _ in range(red):
        new_items[places.pop()]['actual'] = RED
    for _ in range(green):
        new_items[places.pop()]['actual'] = GREEN
    for _ in range(blue):
        new_items[places.pop()]['actual'] = BLUE
    return blue, green, red, new_items


def randomize_colors(times=TIMES_BLUES_MORE_GREENS,
                     all=ITEMS_COUNT):
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
