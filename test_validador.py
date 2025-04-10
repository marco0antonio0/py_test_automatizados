import pytest
from services.validador import validar_idade

def test_idade_valida():
    assert validar_idade(20) is True

def test_idade_negativa():
    with pytest.raises(ValueError, match="Idade inválida"):
        validar_idade(-3)

def test_idade_maior_que_130():
    with pytest.raises(ValueError, match="Idade inválida"):
        validar_idade(140)
