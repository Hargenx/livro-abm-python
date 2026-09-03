"""Modelo de economia simples apresentado no Capítulo 1."""

import math
import random


class Pessoa:
    """Agente que guarda apenas sua riqueza."""

    def __init__(self, riqueza_inicial=100):
        self.riqueza = riqueza_inicial


class Modelo:
    """Modelo que cria os agentes, controla o tempo e observa o sistema."""

    def __init__(self, n=500, riqueza_inicial=100, semente=None):
        if n < 2:
            raise ValueError("O modelo requer pelo menos dois agentes.")

        self.rng = random.Random(semente)
        self.pessoas = [Pessoa(riqueza_inicial) for _ in range(n)]
        self.tempo = 0

    def passo(self):
        """Executa uma rodada da simulação."""
        ativos = [p for p in self.pessoas if p.riqueza > 0]

        for pessoa in ativos:
            pessoa.riqueza -= 1

            outro = self.rng.choice(self.pessoas)

            while outro is pessoa:
                outro = self.rng.choice(self.pessoas)

            outro.riqueza += 1

        self.tempo += 1

    def rodar(self, passos):
        """Executa uma quantidade de passos da simulação."""
        for _ in range(passos):
            self.passo()

    def riquezas(self):
        """Retorna a riqueza de todos os agentes."""
        return [p.riqueza for p in self.pessoas]

    def total(self):
        """Retorna a riqueza total existente no sistema."""
        return sum(self.riquezas())

    def fatias(self):
        """Retorna a fração dos 10% mais ricos e da metade mais pobre."""
        ordenadas = sorted(self.riquezas())

        n = len(ordenadas)
        total = sum(ordenadas) or 1

        quantidade_topo = math.ceil(n * 0.10)
        quantidade_base = n // 2

        topo = sum(ordenadas[-quantidade_topo:])
        base = sum(ordenadas[:quantidade_base])

        return topo / total, base / total

    def gini(self):
        """Calcula o índice de Gini da distribuição de riqueza."""
        ordenadas = sorted(self.riquezas())

        n = len(ordenadas)
        total = sum(ordenadas)

        if total == 0:
            return 0.0

        acumulado = sum((i + 1) * w for i, w in enumerate(ordenadas))

        return (2 * acumulado) / (n * total) - (n + 1) / n
