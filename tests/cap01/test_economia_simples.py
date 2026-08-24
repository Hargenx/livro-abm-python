import pytest

from livro_abm.cap01.economia_simples import Modelo, Pessoa


def test_pessoa_inicia_com_riqueza_informada():
    pessoa = Pessoa(riqueza_inicial=100)

    assert pessoa.riqueza == 100


def test_modelo_inicia_com_configuracao_padrao():
    modelo = Modelo(semente=42)

    assert len(modelo.pessoas) == 500
    assert modelo.tempo == 0
    assert modelo.total() == 50_000
    assert all(pessoa.riqueza == 100 for pessoa in modelo.pessoas)


def test_passo_avanca_o_tempo():
    modelo = Modelo(semente=42)

    modelo.passo()

    assert modelo.tempo == 1


def test_rodar_avanca_o_tempo_corretamente():
    modelo = Modelo(semente=42)

    modelo.rodar(100)

    assert modelo.tempo == 100


def test_riqueza_total_e_conservada():
    modelo = Modelo(n=50, riqueza_inicial=100, semente=42)

    total_inicial = modelo.total()

    modelo.rodar(1000)

    assert modelo.total() == total_inicial


def test_riqueza_nunca_fica_negativa():
    modelo = Modelo(n=50, riqueza_inicial=10, semente=42)

    modelo.rodar(1000)

    assert min(modelo.riquezas()) >= 0


def test_mesma_semente_produz_mesmo_resultado():
    primeiro = Modelo(n=50, riqueza_inicial=100, semente=42)
    segundo = Modelo(n=50, riqueza_inicial=100, semente=42)

    primeiro.rodar(500)
    segundo.rodar(500)

    assert primeiro.riquezas() == segundo.riquezas()


def test_gini_inicial_e_zero():
    modelo = Modelo(semente=42)

    assert modelo.gini() == pytest.approx(0.0)


def test_fatias_na_igualdade_perfeita():
    modelo = Modelo(n=100, riqueza_inicial=100, semente=42)

    topo, base = modelo.fatias()

    assert topo == pytest.approx(0.10)
    assert base == pytest.approx(0.50)
