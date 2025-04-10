import pytest
from services.validar_senha import validar_senha

def test_senha_valida():
    assert validar_senha("senhaForte123") is True

def test_senha_curta():
    with pytest.raises(ValueError, match="Senha muito curta"):
        validar_senha("abc12")

def test_senha_com_8_caracteres():
    assert validar_senha("12345678") is True
