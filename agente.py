"""Atalho supervisionado de execução do assistente de pesquisa.

O código principal fica em `src/`. Quando executado como script, este arquivo
mantém um supervisor mínimo: o trabalho pesado roda em um subprocesso. Se o
Python do trabalhador sofrer falha nativa, como SIGSEGV, o supervisor registra e
reinicia, preservando o estado salvo em `dados/`.
"""
import os
import signal
import subprocess
import sys
import time


def executar_trabalhador():
    from src.motor import principal
    import src.agente as base
    principal(base)


def supervisionar():
    env = os.environ.copy()
    env["AGENTE_WORKER"] = "1"
    reinicios = 0
    while True:
        processo = subprocess.run([sys.executable, __file__, *sys.argv[1:]], env=env)
        codigo = processo.returncode
        if codigo == 0:
            return 0
        if codigo == -signal.SIGINT:
            return 0
        if codigo == -signal.SIGSEGV:
            reinicios += 1
            print(
                f"[supervisor] Trabalhador caiu com SIGSEGV; reiniciando em 5 s "
                f"(reinício {reinicios}). Estado salvo em dados/ será reaproveitado.",
                flush=True,
            )
            time.sleep(5)
            continue
        return codigo


if __name__ == "__main__":
    if os.environ.get("AGENTE_WORKER") == "1":
        executar_trabalhador()
    else:
        raise SystemExit(supervisionar())
else:
    from src.agente import *  # reexporta configuração para compatibilidade
