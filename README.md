# Modelagem Baseada em Agentes em Python

> **Construindo modelos do zero, sem frameworks**

Repositório oficial de código, experimentos, dados e materiais complementares do livro ***Modelagem Baseada em Agentes em Python***, de **Gilberto Gil F. G. Passos, Cristiano Fuschilo e Raphael Mauricio**.

O objetivo deste projeto é tornar todos os modelos apresentados no livro **executáveis, verificáveis e reproduzíveis**, mantendo a proposta pedagógica de construir modelos baseados em agentes a partir de seus componentes fundamentais, sem depender de frameworks de simulação.

---

## 📖 Sobre o livro

Modelagem Baseada em Agentes — **Agent-Based Modeling (ABM)** — é uma abordagem computacional para estudar sistemas nos quais padrões coletivos surgem das interações entre indivíduos.

Em vez de começar pelo comportamento agregado do sistema, construímos os indivíduos que o compõem:

* seu estado;
* aquilo que conseguem perceber;
* suas regras de comportamento;
* suas interações;
* o ambiente;
* e a passagem do tempo.

Depois deixamos o sistema evoluir e observamos os padrões que emergem.

A proposta do livro é aprender ABM **construindo os modelos do zero em Python puro**.

Não utilizamos frameworks de simulação para implementar os modelos centrais do livro. Cada agente, ambiente, regra e mecanismo de escalonamento é escrito explicitamente para que o leitor consiga entender o que está acontecendo em cada etapa da simulação.

> **Quem constrói o motor entende o carro.**

---

## 🎯 Objetivos deste repositório

Este repositório funciona como o **laboratório computacional do livro**.

Aqui serão mantidos:

* códigos utilizados nos capítulos;
* implementações de referência;
* experimentos computacionais;
* notebooks dos exercícios;
* testes automatizados;
* dados utilizados nos experimentos;
* scripts para reprodução das figuras;
* materiais complementares;
* correções e erratas relacionadas aos modelos.

Um dos objetivos principais é garantir que qualquer resultado apresentado no livro possa ser reproduzido a partir do código disponível aqui.

---

## 🧠 Filosofia do projeto

Os exemplos deste repositório seguem alguns princípios.

### 1. O modelo deve ser compreensível

Preferimos implementações explícitas a abstrações sofisticadas.

O leitor deve conseguir localizar no código:

* onde os agentes são criados;
* onde está o estado de cada agente;
* como as decisões são tomadas;
* quem age primeiro;
* onde entra a aleatoriedade;
* como o ambiente é representado;
* como o tempo avança;
* e como os resultados são medidos.

---

### 2. Algoritmo antes do código

Antes de implementar um modelo, procuramos descrever claramente seu algoritmo.

Em especial, decisões como:

* atualização simultânea ou sequencial;
* ordem das ações;
* escalonamento;
* interação entre agentes;
* tratamento das bordas;
* geração de números aleatórios;

devem ser decisões de modelagem conscientes, e não efeitos acidentais da implementação.

---

### 3. Reprodutibilidade importa

Modelos baseados em agentes são frequentemente estocásticos.

Sempre que aplicável, os modelos permitem controlar a **semente do gerador pseudoaleatório**, permitindo reproduzir uma execução específica.

Ao mesmo tempo, conclusões não devem depender de uma única execução.

Os experimentos do livro procuram utilizar:

* múltiplas sementes;
* medidas agregadas;
* análise da variabilidade;
* comparação entre diferentes configurações de parâmetros.

---

### 4. Verificação antes da interpretação

Um programa que executa sem erros não é necessariamente um modelo correto.

Sempre que possível, utilizamos invariantes e propriedades conhecidas do sistema como testes.

Exemplos:

```text
Economia simples
→ a riqueza total deve permanecer constante

SIR
→ S + I + R deve permanecer constante

Movimento espacial
→ posições devem permanecer dentro das regras definidas pelo modelo
```

Essas propriedades também aparecem como testes automatizados neste repositório.

---

### 5. Modelos são simplificações

Os modelos apresentados aqui não pretendem reproduzir toda a complexidade dos sistemas reais.

Eles funcionam como **laboratórios de mecanismos**.

Um modelo permite perguntar:

> Se estas regras individuais fossem verdadeiras, que comportamento coletivo poderia surgir?

Por isso, cada interpretação deve considerar também aquilo que o modelo **não representa**.

---

# 📚 Organização do conteúdo

O conteúdo acompanha a progressão do livro.

## Capítulo 1 — Pensando com agentes

Introdução aos conceitos fundamentais da modelagem baseada em agentes:

* agentes;
* ambiente;
* regras;
* tempo;
* emergência;
* estocasticidade;
* replicação;
* verificação;
* calibração;
* protocolo ODD.

O capítulo apresenta também o primeiro modelo completo: uma economia mínima baseada em transferências aleatórias de riqueza.

### Exercícios

1. Taxas de natalidade
2. Caça aos cogumelos
3. Economia simples
4. Incêndio florestal
5. Jogo da Vida

---

## Capítulo 2 — A anatomia de um modelo

Construção passo a passo de dois modelos fundamentais:

### Caminhantes aleatórios

Um modelo mínimo para entender:

* estado;
* comportamento;
* ambiente;
* relógio;
* aleatoriedade;
* emergência de padrões estatísticos.

### Modelo de segregação de Schelling

Um clássico das ciências sociais computacionais utilizado para investigar como preferências individuais locais podem produzir padrões coletivos de segregação.

---

## Capítulo 3 — Caderno de modelos

Uma coleção de modelos para implementação e experimentação.

6. DLA — Agregação por difusão
7. Heróis e covardes
8. Segregação de Schelling
9. Telemarketing
10. Propagação de doença — SIR
11. Modelo do casamento
12. Woodhoopoes
13. Ficar ou partir
14. Investidor empresarial
15. El Farol
16. Lobos e ovelhas
17. Flocking
18. Formigas forrageadoras
19. Cães selvagens e alcateias

Esses exercícios enfatizam três etapas:

```text
Algoritmo
   ↓
Implementação
   ↓
Experimento
```

---

## Capítulo 4 — Calibração

Introdução à calibração de modelos baseados em agentes.

Entre os temas abordados:

* verificação;
* calibração;
* validação;
* comparação com dados;
* modelagem orientada por padrões;
* busca em grade;
* múltiplas sementes;
* análise de sensibilidade;
* identificação de parâmetros;
* revisão de modelos quando a calibração falha.

---

## Capítulo 5 — Exercícios de calibração

Aplicação das técnicas do capítulo anterior em diferentes modelos.

20. Woodhoopoes
21. Investidor empresarial
22. SIR — epidemia de 1918
23. Casamento — dados brasileiros
24. Predação — lince e lebre

Os exercícios utilizam tanto referências empíricas quanto benchmarks computacionais.

---

# 🗂️ Estrutura do repositório

A estrutura planejada é:

```text
.
├── README.md
├── LICENSE
├── pyproject.toml
│
├── src/
│   └── livro_abm/
│       ├── cap01/
│       ├── cap02/
│       ├── cap03/
│       ├── cap04/
│       └── cap05/
│
├── notebooks/
│   ├── cap01/
│   ├── cap02/
│   ├── cap03/
│   ├── cap04/
│   └── cap05/
│
├── exercises/
│
├── solutions/
│
├── tests/
│
├── data/
│
├── figures/
│
├── scripts/
│
└── .github/
    └── workflows/
```

### `src/`

Implementações utilizadas para gerar resultados, executar experimentos e produzir figuras.

### `notebooks/`

Material interativo associado aos capítulos e exercícios.

### `exercises/`

Arquivos iniciais e recursos necessários para resolver os exercícios do livro.

### `solutions/`

Implementações de referência dos exercícios.

A política de disponibilização das soluções poderá variar durante o desenvolvimento do livro.

### `tests/`

Testes automatizados e invariantes utilizados para verificar as implementações.

### `data/`

Dados utilizados nos experimentos e exercícios de calibração.

Sempre que possível, cada conjunto de dados possuirá documentação contendo:

* fonte original;
* referência bibliográfica;
* transformação realizada;
* unidades;
* limitações conhecidas;
* informações necessárias para reprodução.

### `figures/`

Figuras produzidas diretamente pelos experimentos computacionais.

### `scripts/`

Scripts auxiliares para:

* executar experimentos;
* validar exemplos;
* gerar figuras;
* reproduzir resultados do livro.

---

# 🚀 Executando os exemplos

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Instale o projeto:

```bash
pip install -e .
```

Para instalar também as ferramentas utilizadas no desenvolvimento:

```bash
pip install -e ".[dev]"
```

---

# 🧪 Testes

Os modelos são acompanhados, sempre que possível, por testes automatizados.

Execute:

```bash
pytest
```

Além de testes tradicionais, utilizamos **invariantes do próprio modelo**.

Por exemplo:

```python
def test_riqueza_total_permanece_constante():
    modelo = Modelo(semente=42)

    total_inicial = modelo.total()

    modelo.rodar(1000)

    assert modelo.total() == total_inicial
```

Em modelos estocásticos, também verificamos a reprodutibilidade:

```python
def test_mesma_semente_produz_mesmo_resultado():
    a = Modelo(semente=42)
    b = Modelo(semente=42)

    a.rodar(1000)
    b.rodar(1000)

    assert a.riquezas() == b.riquezas()
```

---

# 🎲 Sobre aleatoriedade

Uma execução individual de um modelo estocástico representa apenas **uma possível história do sistema**.

Por isso existem dois usos diferentes para sementes:

### Reprodução

Uma semente fixa permite reproduzir exatamente uma execução:

```python
modelo = Modelo(semente=42)
```

### Experimentação

Para estudar o comportamento do modelo, devemos executar várias sementes:

```python
for semente in range(30):
    modelo = Modelo(semente=semente)
    ...
```

As conclusões devem considerar a distribuição dos resultados, e não apenas uma execução isolada.

---

# 📊 Reprodução das figuras

Sempre que possível, as figuras utilizadas no livro serão geradas diretamente a partir dos códigos deste repositório.

A intenção é manter o seguinte fluxo:

```text
modelo
  ↓
experimento
  ↓
resultado
  ↓
figura
  ↓
livro
```

Dessa forma, código, resultado e figura permanecem sincronizados.

---

# 📓 Notebooks

Os notebooks são utilizados como ambiente de experimentação.

Um notebook de exercício pode conter:

1. descrição do problema;
2. algoritmo ou pseudocódigo;
3. implementação;
4. experimento;
5. visualizações;
6. análise dos resultados;
7. respostas às perguntas propostas.

Os notebooks não substituem as implementações de referência presentes em `src/`. Eles funcionam como ambiente didático para investigação.

---

# 📦 Dependências

A filosofia do livro é manter os modelos tão próximos quanto possível do **Python padrão**.

Bibliotecas externas são utilizadas principalmente quando oferecem suporte à:

* visualização;
* testes;
* análise;
* infraestrutura de desenvolvimento.

A implementação conceitual dos agentes e mecanismos de simulação permanece explícita.

---

# 🔬 Reprodutibilidade científica

Este repositório também funciona como registro computacional dos experimentos apresentados no livro.

Nosso objetivo é que cada resultado relevante possa ser associado a:

* versão do código;
* parâmetros utilizados;
* sementes;
* dados de entrada;
* método de análise;
* figura resultante.

Resultados numéricos apresentados no livro deverão, sempre que possível, poder ser regenerados a partir deste repositório.

---

# 📑 Dados e proveniência

Dados empíricos utilizados no livro devem possuir sua origem documentada.

Quando um conjunto de dados tiver sido:

* transcrito;
* agregado;
* normalizado;
* convertido;
* aproximado;
* reconstruído;

a transformação será explicitamente registrada.

A presença dos dados neste repositório não implica necessariamente que eles possam ser redistribuídos. Quando houver restrições de licença, serão disponibilizadas apenas instruções para obtenção da fonte original.

---

# ✅ Status do projeto

> **Livro em desenvolvimento.**

O conteúdo, as APIs e a organização do repositório ainda podem mudar durante a revisão técnica da obra.

A revisão atual inclui:

* validação das implementações;
* reprodução dos experimentos;
* auditoria dos valores apresentados no texto;
* revisão da origem dos dados;
* testes automatizados;
* revisão das referências metodológicas.

Encontrou alguma inconsistência entre o livro e o código?

Abra uma **Issue**.

---

# 🐛 Erratas

Erros encontrados após a publicação de uma versão do livro serão registrados neste repositório.

Quando aplicável, uma errata deverá indicar:

```text
Versão do livro
Capítulo
Seção
Página

Texto atual
Correção
Impacto sobre código/resultados
```

Veja:

**[ERRATA.md](./ERRATA.md)**

---

# 🤝 Contribuições

Correções e sugestões são bem-vindas.

Alguns exemplos:

* erro em código;
* resultado que não pode ser reproduzido;
* referência incorreta;
* erro matemático;
* comportamento inesperado de uma implementação;
* problema em um conjunto de dados;
* melhoria de documentação.

Antes de enviar um Pull Request, consulte:

**[CONTRIBUTING.md](./CONTRIBUTING.md)**

Para erros relacionados diretamente ao conteúdo do livro, prefira abrir uma **Issue** descrevendo:

1. capítulo e seção;
2. comportamento ou texto observado;
3. resultado esperado;
4. código mínimo para reprodução, quando aplicável.

---

# 📚 Referências fundamentais

Entre as principais referências utilizadas na construção do material estão:

* Schelling, T. C. (1971). *Dynamic Models of Segregation*.
* Schelling, T. C. (1978). *Micromotives and Macrobehavior*.
* Epstein, J. M.; Axtell, R. (1996). *Growing Artificial Societies*.
* Wilensky, U.; Rand, W. (2015). *An Introduction to Agent-Based Modeling*.
* Railsback, S. F.; Grimm, V. (2019). *Agent-Based and Individual-Based Modeling: A Practical Introduction*.
* Grimm, V. et al. (2006). *A Standard Protocol for Describing Individual-Based and Agent-Based Models*.
* Grimm, V. et al. (2010). *The ODD Protocol: A Review and First Update*.

A bibliografia completa é apresentada no livro.

---

# ✍️ Autores

**Gilberto Gil F. G. Passos**

**Cristiano Fuschilo**

**Raphael Mauricio**

---

# 📖 Como citar

A referência bibliográfica definitiva será disponibilizada após a publicação do livro.

Durante o período de desenvolvimento, utilize:

```bibtex
@book{passos_fuschilo_mauricio_abm,
  title     = {Modelagem Baseada em Agentes em Python:
               construindo modelos do zero, sem frameworks},
  author    = {Passos, Gilberto Gil F. G. and
               Fuschilo, Cristiano and
               Mauricio, Raphael},
  note      = {Livro em desenvolvimento}
}
```

Quando houver DOI ou ISBN, esta seção será atualizada.

---

# 📄 Licença

A licença definitiva do conteúdo, dos códigos e dos materiais do livro será definida antes da publicação.

Observe que **código-fonte, texto do livro, figuras e dados podem possuir políticas de licenciamento diferentes**.

Consulte o arquivo:

**[LICENSE](./LICENSE)**

antes de redistribuir qualquer material.

---

## ⭐ Acompanhe o projeto

Se este material for útil para seus estudos, aulas ou pesquisas, considere marcar o repositório com uma ⭐.

Isso ajuda outras pessoas interessadas em:

**Agent-Based Modeling · Python · Sistemas Complexos · Simulação Computacional · Ciência Computacional**

a encontrar o projeto.
