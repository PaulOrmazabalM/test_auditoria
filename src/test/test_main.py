import pytest
from src.main import sumar




@pytest.mark.parametrize(
    "input_a,input_b,esperado",
[
    (2,3,5),
    (5,5,10),
    (3,3,6),
    (sumar(4,2),6,12),
]
)

def test_suma(input_a,input_b,esperado):
    assert sumar(input_a,input_b)==esperado

def test_sumar():
    assert sumar(6,6)==12




