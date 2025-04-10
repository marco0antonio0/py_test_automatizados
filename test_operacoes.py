import pytest
from services.operacoes import multiplica, divide

def test_multiplicacao_positivos():
    assert multiplica(3, 4) == 12

def test_multiplicacao_com_zero():
    assert multiplica(5, 0) == 0

def test_divisao_valida():
    assert divide(10, 2) == 5.0

def test_divisao_por_zero():
    with pytest.raises(ValueError, match="Divisão por zero"):
        divide(10, 0)
