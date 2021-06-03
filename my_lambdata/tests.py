import random

from .my_mod import enlarge

def test_enlarge():
    x0 = 0.1
    y0 = enlarge(x0)
    assert y0 == 10

    x1 = random.randint(100,10000)
    y1 = enlarge(x1)
    assert y1 == x1 * 100

from .fibo import *

def test_fib2():
    x0 = 100
    y0 = fib2(x0)
    assert len(y0) == 12