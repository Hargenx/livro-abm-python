import pytest

from livro_abm.cap01.economia_simples import Modelo


@pytest.mark.slow
def test_reproduz_figura_1_1():
    """Reproduz os valores de Gini apresentados na Figura 1.1."""
    modelo = Modelo(semente=1)

    resultados_esperados = {
        100: 0.056,
        1_000: 0.178,
        5_000: 0.339,
        50_000: 0.484,
    }

    for rodada, gini_esperado in resultados_esperados.items():
        modelo.rodar(rodada - modelo.tempo)

        assert round(modelo.gini(), 3) == gini_esperado


@pytest.mark.slow
def test_reproduz_fatias_da_rodada_5000():
    """Reproduz as fatias de riqueza descritas no texto do Capítulo 1."""
    modelo = Modelo(semente=1)

    modelo.rodar(5_000)

    topo, base = modelo.fatias()

    assert topo == pytest.approx(0.21524)
    assert base == pytest.approx(0.25586)
