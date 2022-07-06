from cmath import sqrt as sqrt_imaginary
from math import sqrt
from typing import Tuple, Union, List, Dict
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

