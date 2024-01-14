import pytest
from src.main import sumar
from src.main import validar_usuario


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



def test_validar_usuario_correcto():
    assert validar_usuario("usuario1", "contraseña123") is True

def test_validar_usuario_incorrecto():
    assert validar_usuario("usuario1", "clave456") is False

def test_validar_usuario_no_existente():
    assert validar_usuario("usuario_no_existente", "contraseña123") is False

def test_validar_contraseña_incorrecta():
    assert validar_usuario("usuario1", "contraseña_incorrecta") is False



