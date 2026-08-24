# Contributing

Obrigado pelo interesse em contribuir com o projeto **Modelagem Baseada em Agentes em Python**.

Este repositório acompanha o desenvolvimento de um livro e, por isso, recebe contribuições de naturezas diferentes:

* correções de código;
* testes;
* problemas de reprodutibilidade;
* correções matemáticas;
* inconsistências entre código e texto;
* referências bibliográficas;
* problemas em conjuntos de dados;
* documentação;
* sugestões didáticas;
* erratas.

Contribuições são bem-vindas, mas o objetivo principal é manter o conteúdo
**correto, reproduzível, didático e coerente com a proposta do livro**.

---

# Antes de contribuir

Verifique primeiro se já existe uma **Issue** tratando do mesmo assunto.

Caso não exista, considere abrir uma antes de realizar mudanças significativas.

Correções pequenas e evidentes podem ser enviadas diretamente por Pull Request.

Mudanças conceituais, metodológicas ou estruturais devem ser discutidas antes.

---

# Tipos de contribuição

## 1. Erros de código

Exemplos:

* erro de sintaxe;
* função inexistente;
* comportamento diferente do descrito no livro;
* resultado incompatível com a figura apresentada;
* uso incorreto de uma API;
* erro de inicialização;
* comportamento não reprodutível quando deveria ser.

Ao relatar o problema, inclua preferencialmente:

```text
Capítulo:
Seção:
Arquivo:
Versão/commit:
Python:
Sistema operacional:
Seed:
Parâmetros utilizados:
Resultado observado:
Resultado esperado:
```

Se possível, inclua um exemplo mínimo para reprodução.

---

## 2. Erros matemáticos

Incluem:

* fórmula incorreta;
* cálculo errado;
* valor de referência incompatível com o modelo;
* interpretação estatística equivocada;
* unidade incorreta.

Ao propor uma correção, apresente o raciocínio ou referência utilizada.

Correções matemáticas devem, sempre que possível, ser acompanhadas por um
teste automatizado.

---

## 3. Problemas de reprodutibilidade

Uma contribuição deste tipo é particularmente importante.

Informe:

* comando executado;
* commit utilizado;
* parâmetros;
* seed ou conjunto de seeds;
* resultado encontrado;
* resultado publicado no livro ou repositório;
* ambiente de execução.

Resultados estocásticos não precisam ser numericamente idênticos entre seeds
diferentes.

Quando a reprodução depender de uma seed específica, isso deve estar
explicitamente documentado.

---

## 4. Dados e fontes

Problemas envolvendo dados podem incluir:

* fonte incorreta;
* transcrição errada;
* dado sem proveniência;
* transformação não documentada;
* unidade incorreta;
* licença incompatível;
* dado histórico atribuído à fonte errada.

Ao propor uma fonte, forneça preferencialmente:

```text
Autor ou instituição:
Título:
Ano:
Publicação:
DOI:
URL:
Tabela/página:
Observação:
```

Não envie arquivos de terceiros cuja redistribuição não seja permitida.

---

## 5. Referências científicas

Referências adicionais são bem-vindas quando ajudam a:

* corrigir uma afirmação;
* atualizar uma metodologia;
* documentar a origem de um modelo;
* fornecer evidência para uma escolha de modelagem;
* esclarecer limitações.

Dê preferência a:

1. artigos científicos revisados por pares;
2. livros acadêmicos reconhecidos;
3. documentação oficial;
4. bases de dados institucionais;
5. fontes primárias.

Evite substituir uma fonte primária por uma fonte secundária quando a primeira
estiver disponível.

---

## 6. Melhorias didáticas

O projeto aceita sugestões pedagógicas, incluindo:

* explicações mais claras;
* exemplos melhores;
* exercícios;
* visualizações;
* perguntas para discussão;
* pequenas reorganizações.

Entretanto, o livro segue uma filosofia específica:

> compreender o modelo construindo seus mecanismos explicitamente.

Por isso, contribuições não devem substituir modelos didáticos por frameworks
ou abstrações que escondam os conceitos que o exemplo pretende ensinar.

Frameworks de ABM podem aparecer como material complementar, mas não devem
substituir a implementação conceitual dos modelos centrais.

---

# Fluxo recomendado

Para mudanças de código:

```text
Issue
  ↓
Discussão, se necessária
  ↓
Branch
  ↓
Implementação
  ↓
Testes
  ↓
Pull Request
  ↓
Revisão
```

---

# Configurando o ambiente

Clone o projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative-o.

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Instale o projeto em modo de desenvolvimento:

```bash
pip install -e ".[dev]"
```

---

# Qualidade de código

Antes de enviar um Pull Request, execute:

```bash
ruff check .
```

e:

```bash
pytest
```

Se o projeto utilizar verificação de tipos no módulo alterado:

```bash
mypy src/
```

Todos os testes existentes devem continuar passando.

---

# Estilo de código

O código deve priorizar:

1. clareza;
2. correção;
3. reprodutibilidade;
4. proximidade com o conceito ensinado;
5. desempenho.

Performance é importante em simulações, mas não deve tornar um exemplo
introdutório desnecessariamente difícil de compreender.

Evite otimizações prematuras.

---

# Números aleatórios

Sempre que possível, evite depender diretamente do estado global de
aleatoriedade.

Prefira um gerador associado ao modelo:

```python
import random


class Modelo:
    def __init__(self, semente=None):
        self.rng = random.Random(semente)
```

e depois:

```python
valor = self.rng.random()
```

Isso facilita:

* reprodução;
* testes;
* múltiplas simulações;
* execução paralela;
* investigação de bugs.

---

# Testes

Existem diferentes tipos de propriedades interessantes em modelos baseados em
agentes.

## Invariantes

Exemplo:

```python
def test_riqueza_e_conservada():
    modelo = Modelo(semente=42)

    inicial = modelo.total()
    modelo.rodar(100)

    assert modelo.total() == inicial
```

## Limites

Exemplo:

```python
def test_riqueza_nunca_e_negativa():
    modelo = Modelo(semente=42)

    modelo.rodar(1000)

    assert min(modelo.riquezas()) >= 0
```

## Reprodutibilidade

```python
def test_mesma_semente_mesmo_resultado():
    a = Modelo(semente=42)
    b = Modelo(semente=42)

    a.rodar(500)
    b.rodar(500)

    assert a.estado() == b.estado()
```

## Casos-limite

Sempre que relevante, teste situações como:

* zero agentes;
* um único agente;
* população muito pequena;
* parâmetros nos limites;
* nenhum recurso;
* todos os agentes no mesmo estado;
* ausência de eventos possíveis.

---

# Testes para comportamento estocástico

Evite testes frágeis como:

```python
assert media == 10.438275
```

quando o valor é um resultado estatístico.

Prefira:

* invariantes determinísticos;
* tolerâncias justificadas;
* propriedades esperadas;
* testes com seeds fixas;
* testes sobre distribuições quando apropriado.

Não escolha uma tolerância apenas para fazer o teste passar.

---

# Pull Requests

Um Pull Request deve ter escopo limitado e descrição clara.

Um bom título:

```text
fix: corrige conservação de riqueza no modelo do capítulo 1
```

Outros prefixos recomendados:

```text
fix:
feat:
docs:
test:
refactor:
data:
figure:
ci:
```

Na descrição, informe:

### Problema

O que estava errado?

### Alteração

O que foi modificado?

### Verificação

Como a correção foi testada?

### Impacto no livro

Marque uma das opções:

* [ ] Nenhum
* [ ] Código apresentado no livro
* [ ] Resultado numérico
* [ ] Figura
* [ ] Texto
* [ ] Exercício
* [ ] Referência
* [ ] Dataset
* [ ] Errata necessária

---

# Alterações que afetam resultados publicados

Mudanças que alterem resultados do livro exigem atenção especial.

Por exemplo:

```text
seed 42:

antes
Gini = 0.48

depois
Gini = 0.41
```

Nesse caso, o Pull Request deve explicar:

1. por que o resultado mudou;
2. se o resultado antigo estava errado;
3. quais figuras são afetadas;
4. quais trechos do livro precisam ser revisados;
5. se deve existir entrada em `ERRATA.md`.

Nunca atualize silenciosamente um resultado científico.

---

# Alterações em datasets

Toda alteração de dados deve registrar:

```text
Origem:
Versão anterior:
Versão nova:
Motivo:
Transformação:
Impacto:
```

Se possível, preserve o dado original separadamente do dado processado.

Exemplo:

```text
data/
└── exemplo/
    ├── raw/
    ├── processed/
    └── README.md
```

---

# Notebooks

Notebooks devem:

* executar do início ao fim;
* evitar estado oculto;
* utilizar seeds explícitas quando relevante;
* conter apenas saídas necessárias;
* não depender de arquivos locais não versionados.

Antes de enviar:

```text
Restart Kernel
↓
Run All
```

e confirme que nenhuma célula falha.

---

# Figuras

Uma figura usada no livro deve ser reproduzível.

Sempre que possível, ela deve ser gerada por um script versionado:

```bash
python scripts/gerar_figuras.py
```

Evite alterações manuais posteriores que não possam ser reproduzidas pelo
código.

---

# Correções editoriais

Correções de ortografia e formatação podem ser propostas normalmente.

Para mudanças que alterem significado científico, abra primeiro uma Issue.

Exemplos:

* interpretação de um modelo;
* afirmação histórica;
* definição científica;
* explicação estatística;
* descrição de um dataset;
* comparação entre metodologias.

---

# Compatibilidade com o livro

O repositório pode estar à frente da versão publicada do livro.

Quando isso acontecer, as diferenças relevantes deverão ser documentadas.

Consulte:

```text
ERRATA.md
```

para correções conhecidas.

---

# Commit messages

Mensagens claras facilitam a revisão.

Exemplos:

```text
fix: adiciona método ranking ao modelo de riqueza

test: verifica conservação da população no SIR

docs: documenta origem dos dados do IBGE

data: corrige transcrição da série histórica

figure: regenera gráfico de Schelling

refactor: usa gerador aleatório local no caminhante
```

Evite mensagens genéricas como:

```text
update
changes
fix stuff
teste
novo
```

---

# Conduta científica

Contribuições devem seguir alguns princípios simples:

* não esconder resultados desfavoráveis;
* não selecionar seeds apenas porque produzem o resultado esperado;
* não alterar tolerâncias depois de observar os resultados sem documentar;
* não modificar dados para melhorar uma calibração;
* não apresentar benchmark sintético como evidência empírica;
* distinguir hipótese, resultado do modelo e fato observado;
* informar limitações relevantes.

---

# Autoria e licenciamento

Ao enviar uma contribuição, você declara que possui direito de disponibilizar
o material enviado.

Contribuições de código serão aceitas sob os termos definidos em `LICENSE`.

Sugestões e correções editoriais poderão ser incorporadas ao manuscrito pelos
autores.

Quando uma contribuição intelectual substancial justificar reconhecimento
adicional, isso poderá ser discutido com os autores.

---

# Dúvidas

Se não souber se uma contribuição deve ser:

* Issue;
* Pull Request;
* errata;
* discussão;

abra uma Issue descrevendo o caso.

É melhor discutir uma mudança antes do que corrigir silenciosamente algo que
tenha implicações científicas.
