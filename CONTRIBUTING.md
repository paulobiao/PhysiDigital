# Contributing to PhysiDigital™

## Fluxo
- Fork → branch `feat/...` → PR
- Commits descritivos e pequenos
- Testes mínimos para funções novas

## Padrão de código
- Python 3.11+
- PEP8 + docstrings breves
- Dados de sensores são **sintéticos** (não usar dados reais/sensíveis)

## Rodando local
```bash
pip install -r requirements.txt
uvicorn src.physidigital.main:app --reload --port 8000
# docs: http://localhost:8000/docs
