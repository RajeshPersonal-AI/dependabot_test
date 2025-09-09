from app.math_utils import add, mul

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_mul():
    assert mul(2, 4) == 8
    assert mul(-3, 3) == -9
