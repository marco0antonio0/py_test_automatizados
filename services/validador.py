def validar_idade(idade):
    if idade < 0 or idade > 130:
        raise ValueError("Idade inválida")
    return True
