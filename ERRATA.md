# Errata

Este documento registra correções conhecidas do livro:

# Modelagem Baseada em Agentes em Python

**Construindo modelos do zero, sem frameworks**

Autores:

* Gilberto Gil F. G. Passos
* Cristiano Fuschilo
* Raphael Mauricio

---

## Sobre esta errata

Nosso objetivo é manter um registro transparente de erros identificados após a
disponibilização de versões do livro.

Uma correção pode envolver:

* texto;
* código;
* fórmula;
* figura;
* resultado numérico;
* exercício;
* dataset;
* referência;
* interpretação científica.

Correções não são removidas silenciosamente deste documento após serem
incorporadas a uma nova versão.

Elas permanecem registradas para que leitores de versões anteriores consigam
identificar o que mudou.

---

# Como identificar sua versão

Consulte a página inicial do livro.

Versões preliminares poderão ser identificadas por:

```text
data
número da versão
commit/tag associado
```

Quando a publicação definitiva existir, esta seção será atualizada com:

* edição;
* ISBN;
* data de publicação;
* impressão, quando aplicável.

---

# Classificação

Utilizamos quatro níveis.

## 🟢 Editorial

Não altera o conteúdo técnico.

Exemplos:

* ortografia;
* pontuação;
* referência cruzada;
* formatação;
* nome de variável no texto.

---

## 🟡 Técnica

Existe um erro técnico, mas ele não altera a principal conclusão apresentada.

Exemplos:

* código incompleto;
* comentário incorreto;
* unidade;
* pequeno erro numérico;
* definição excessivamente ampla.

---

## 🟠 Substantiva

Altera um resultado, explicação ou interpretação relevante.

Exemplos:

* fórmula incorreta;
* figura gerada por código errado;
* resultado numérico incorreto;
* interpretação metodológica equivocada;
* parâmetro errado.

---

## 🔴 Crítica

Compromete uma conclusão, exercício empírico ou atribuição científica.

Exemplos:

* dataset atribuído à fonte errada;
* evidência inexistente;
* conclusão incompatível com o modelo;
* erro que invalida um experimento;
* problema grave de proveniência.

---

# Erratas confirmadas

> Esta seção deve conter somente erros já verificados pelos autores.

---

## ERR-001 — [Título curto]

**Status:** exemplo de estrutura
**Severidade:** 🟡 Técnica
**Versão afetada:** —
**Capítulo:** —
**Seção:** —
**Página:** —

### Como está

> Texto ou descrição incorreta.

### Correção

> Texto ou descrição corrigida.

### Motivo

Explique objetivamente por que o conteúdo anterior estava incorreto.

### Impacto

* Código: não
* Figura: não
* Resultado: não
* Interpretação: não

### Corrigido em

```text
commit:
tag:
versão:
```

---

# Formato para novas entradas

Use o seguinte modelo:

```markdown
## ERR-XXX — Título

**Status:** confirmada
**Severidade:** 🟢 / 🟡 / 🟠 / 🔴
**Versão afetada:**
**Capítulo:**
**Seção:**
**Página:**

### Como está

> ...

### Correção

> ...

### Motivo

...

### Impacto

- Código:
- Figura:
- Resultado:
- Interpretação:
- Exercícios relacionados:

### Corrigido em

commit:
tag:
versão:
```

---

# Correções identificadas durante a revisão técnica

As entradas abaixo são destinadas à revisão da versão preliminar e ainda
devem ser verificadas e formalizadas antes de serem consideradas erratas
definitivas.

Elas podem ser transferidas para **Erratas confirmadas** após revisão pelos
autores.

---

## CANDIDATA — Modelo de riqueza utiliza `ranking()`

**Status:** em revisão
**Severidade estimada:** 🟡 Técnica
**Capítulo:** 1
**Seção:** Desigualdade não é imobilidade

O exemplo utiliza:

```python
m.ranking()
```

A revisão do código deve confirmar se o método está definido na implementação
oficial.

Caso esteja ausente, será necessário:

* implementá-lo;
* ou substituir o exemplo por código já pertencente à API apresentada.

---

## CANDIDATA — Formulação da fertilidade

**Status:** em revisão
**Severidade estimada:** 🟠 Substantiva
**Capítulo:** 1
**Exercício:** Taxas de natalidade

A versão preliminar contém uma explicação quantitativa da evolução relativa das
duas populações que deve ser reavaliada matematicamente e comparada à
implementação oficial.

A correção definitiva será registrada após a revisão do modelo e dos valores
de referência.

---

## CANDIDATA — Uso do gerador aleatório nos caminhantes

**Status:** em revisão
**Severidade estimada:** 🟡 Técnica
**Capítulo:** 2
**Seção:** Caminhantes aleatórios

A implementação deve ser revisada para verificar consistência com a convenção
adotada pelo restante do livro:

```python
self.rng = random.Random(semente)
```

A mudança poderá afetar a sequência exata de resultados utilizada na figura,
embora não necessariamente o comportamento estatístico do modelo.

---

## CANDIDATA — Fonte dos dados de Boston, 1918

**Status:** em revisão
**Severidade estimada:** 🔴 Crítica
**Capítulo:** 4 e Capítulo 5
**Modelo:** SIR

A origem da série histórica utilizada no exercício deve ser confirmada
diretamente na fonte primária.

Antes de publicar uma correção definitiva, devem ser registrados:

* fonte exata;
* tabela ou página;
* variável observada;
* unidade;
* período;
* transformação aplicada.

Até que a proveniência seja confirmada, o conjunto não deve ser tratado como
validado documentalmente.

---

## CANDIDATA — Conversão entre mortalidade e infectados

**Status:** em revisão
**Severidade estimada:** 🟠 Substantiva
**Capítulo:** 4 e Capítulo 5
**Modelo:** SIR

O exercício utiliza mortalidade observada para comparação com infectados
produzidos pelo modelo.

A revisão deve definir explicitamente:

* se a mortalidade será utilizada apenas como proxy de forma;
* se haverá transformação para incidência;
* qual atraso temporal será assumido;
* quais conclusões epidemiológicas são permitidas.

A hipótese adotada deverá ser documentada como simplificação do exercício.

---

## CANDIDATA — Relação histórica entre lince/lebre e Lotka–Volterra

**Status:** em revisão
**Severidade estimada:** 🟠 Substantiva
**Capítulo:** 5
**Exercício:** Predação

A descrição histórica da relação entre a série lince–lebre e o desenvolvimento
das equações de Lotka–Volterra deve ser verificada em fontes históricas
adequadas.

A correção deve distinguir entre:

* origem histórica do modelo;
* aplicação posterior do modelo;
* uso didático contemporâneo da série.

---

# Issues abertas

Problemas ainda não confirmados devem preferencialmente permanecer como Issues
no GitHub.

Esta seção poderá apontar para a busca:

```text
label:errata
```

Não registre como erro confirmado algo que ainda esteja em investigação.

---

# Errata e código

Quando uma correção textual decorrer de um bug no código, a entrada deve
registrar ambos.

Exemplo:

```text
Livro:
Figura 2.3 incorreta.

Código:
ordem de atualização estava errada.

Correção:
commit abc123

Consequência:
figura regenerada e valores da seção alterados.
```

Isso mantém uma trilha entre:

```text
erro
  ↓
causa
  ↓
correção no código
  ↓
novo experimento
  ↓
correção no livro
```

---

# Errata e reprodutibilidade

Uma diferença numérica não constitui automaticamente uma errata.

Em modelos estocásticos, deve-se verificar:

* versão do código;
* parâmetros;
* número de execuções;
* seeds;
* estatística utilizada;
* tolerância esperada.

Uma diferença somente deve ser registrada como erro quando houver evidência de
que o resultado publicado:

* não pode ser reproduzido pelas condições declaradas;
* foi calculado incorretamente;
* resultou de uma implementação posteriormente identificada como incorreta.

---

# Errata e novas edições

Quando uma correção já estiver incorporada a uma edição posterior:

```text
Status: corrigida
```

mas a entrada permanecerá neste documento.

Exemplo:

```text
Afeta:
versão 0.1
versão 0.2

Corrigido:
versão 0.3
```

---

# Reportando um novo erro

Se você identificar um possível erro, abra uma Issue contendo:

```text
Título:
[Errata] descrição curta

Versão do livro:
Capítulo:
Seção:
Página:

Conteúdo observado:

Conteúdo esperado:

Justificativa:

Referência, quando aplicável:

Código para reprodução, quando aplicável:
```

Não é necessário ter certeza de que se trata de um erro.

Investigações também são bem-vindas.

---

# Agradecimentos

Agradecemos a leitores, estudantes, professores e pesquisadores que dedicarem
tempo à reprodução dos modelos e ao relato de inconsistências.

Em um livro sobre simulação computacional, **reprodutibilidade também faz parte
do conteúdo que queremos ensinar**.
