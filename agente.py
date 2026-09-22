"""Atalho de execução do assistente de pesquisa.

O código principal fica em `src/` para manter a raiz do projeto limpa.
Use normalmente:

    python agente.py
"""
import sys

from src.agente import *  # reexporta configuração para compatibilidade
from src.motor import principal


if __name__ == "__main__":
    principal(sys.modules["src.agente"])
