# ✅ Testes com Pytest

Este projeto contém testes automatizados usando o framework [pytest](https://docs.pytest.org/). Os testes cobrem validações de senha, idade e operações matemáticas básicas.

---

## 📦 Requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes)

---

## 🛠️ Instalação do pytest

Você pode instalar o `pytest` com o seguinte comando:

```bash
pip install pytest
```

Se estiver usando um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install pytest
```

---

## ▶️ Executando os testes

Para rodar **todos os testes** do projeto:

```bash
pytest
```

Para rodar os testes com mais detalhes:

```bash
pytest -v
```

Para rodar apenas um arquivo específico:

```bash
pytest ./test_validar_senha.py
```

---

## 📁 Estrutura dos arquivos

```
project/
├── services/
│   ├── validar_senha.py
│   ├── validador.py
│   └── operacoes.py
├── test_validar_senha.py
├── test_validador.py
├── test_operacoes.py
└── .gitignore
```

---

## 📄 Observações

- O diretório `__pycache__` e `.pytest_cache/` estão ignorados via `.gitignore`.
- Os testes são organizados na pasta `tests/`, separados por responsabilidade.
- As funções testadas estão no diretório `services/`.

---

Feito com 💻 por Marco Antonio
