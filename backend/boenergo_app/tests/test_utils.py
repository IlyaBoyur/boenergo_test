import pytest
from boenergo_app.utils import calculate_square_roots


@pytest.mark.parametrize(
    'a, b, c, expected',
    ([4, 4, 1, (-0.5, -0.5,)],
     [1, 5, 4, (-1, -4,)],
     [4, 5, 1, (-0.25, -1,)],
     [1, 2, 5, (-1+2j, -1-2j,)],
     [5, 2, 1, (-0.2+0.4j, -0.2-0.4j,)],)
)
def test_calculate_square_roots(a, b, c, expected):
    assert calculate_square_roots(a,b,c) == expected
