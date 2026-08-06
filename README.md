# Exercicios de Algoritmos e Programacao de Computadores

Colecao de 90 questoes individuais da disciplina **Algoritmos e Programacao de Computadores (APC)** do Departamento de Ciencia da Computacao da Universidade de Brasilia, organizadas em 9 topicos progressivos (de declaracao de variaveis ate manipulacao de arquivos), somando 10 questoes por topico. 88 delas sao exercicios de programacao em Python, com um `Resposta N.py` executavel; as outras 2 sao questoes de multipla escolha/resposta curta do mesmo estilo CodeRunner/Moodle, sem codigo para escrever. Todas as 88 questoes de programacao foram validadas de verdade contra os casos de exemplo fornecidos, nao apenas revisadas por leitura de codigo.

> Este repositorio reune apenas os exercicios individuais. Os dois projetos maiores da mesma disciplina, que integram varios desses topicos em programas completos, estao em [Trabalhos-Algoritmos-Progamacao-Computadores](https://github.com/GustavoVieiraDeAraujo/Trabalhos-Algoritmos-Progamacao-Computadores).

---

## Sumario

- [Exercicios de Algoritmos e Programacao de Computadores](#exercicios-de-algoritmos-e-programacao-de-computadores)
  - [Sumario](#sumario)
  - [Participantes](#participantes)
  - [Tecnologias](#tecnologias)
  - [Formato de Cada Exercicio](#formato-de-cada-exercicio)
  - [Estrutura do Projeto](#estrutura-do-projeto)
  - [Requisitos](#requisitos)
  - [Como Executar](#como-executar)
  - [Exercicios por Topico](#exercicios-por-topico)

---

## Participantes

| Nome | Matricula |
|---|---|
| Gustavo Vieira de Araujo | 211068440 |

---

## Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3 | Linguagem de implementacao de todos os exercicios |
| `collections.Counter` | Contagem de componentes conexos (Dicionarios e Tuplas, Questao 9) |
| `csv` (biblioteca padrao) | Leitura de arquivos delimitados em exercicios da pasta Arquivos |

---

## Formato de Cada Exercicio

Cada uma das 90 pastas `Questão N/` segue sempre a mesma estrutura de 3 arquivos:

| Arquivo | Conteudo |
|---|---|
| `Enunciado N.PNG` | Especificacao original do problema, como imagem (formato de entrada, regras de negocio, restricoes) |
| `Exemplos N.PNG` | Tabela com pares de entrada/saida esperados, usada tanto para resolver quanto para validar a solucao |
| `Resposta N.py` (ou `Resposta N (marcada).py`) | Script Python autocontido que le a entrada via `stdin` e imprime a saida no formato exigido pelo enunciado |

O sufixo `(marcada)` identifica arquivos que o proprio autor, na epoca da resolucao, sinalizou como possivelmente incorretos (geralmente por desconfianca da propria logica, nao por erro reportado por um corretor automatico). Das poucas dezenas de arquivos com esse sufixo, a maioria das suspeitas se confirmou como bug real, ver [Bugs Corrigidos](#bugs-corrigidos) e [Processo de Validacao](#processo-de-validacao).

**Excecao**: `Funções/Questão 3` e `Variaveis e Expressões/Questão 1` nao seguem esse padrao porque nao sao exercicios de escrever codigo; sao questoes de multipla escolha/resposta curta (analisar um trecho pronto e marcar o comportamento correto, ou calcular um valor numerico direto), no mesmo estilo CodeRunner/Moodle das demais. A resposta certa ja vem marcada com um check verde na propria imagem `Enunciado e Resposta N.PNG`, entao nao ha um `Resposta N.py` separado nem nada para executar. Por nao serem codigo, essas 2 questoes nao passaram pela validacao por execucao ao vivo descrita em [Processo de Validacao](#processo-de-validacao); as outras 88, que sao todas exercicios de programacao de verdade, sim.

---

## Estrutura do Projeto

| Diretorio | Questoes | Conceitos praticados |
|---|---|---|
| `Variaveis e Expressões/` | 10 | Declaracao de variaveis, tipos primitivos, precedencia de operadores, avaliacao de expressoes aritmeticas e logicas |
| `Condicionais e Recursividade/` | 10 | `if`/`elif`/`else`, condicoes compostas, funcoes recursivas (incluindo casos-base e chamadas com acumulador) |
| `Funções/` | 10 | Definicao e chamada de funcoes sem valor de retorno (efeito colateral via `print`), passagem de parametros |
| `Funções com Resultado/` | 10 | Funcoes que retornam valores, incluindo retornos multiplos (tuplas) e composicao de funcoes |
| `Iterações/` | 10 | Lacos `while` e `for`, acumuladores, condicoes de parada, iteracao sobre entrada de tamanho indeterminado |
| `Strings/` | 10 | Fatiamento, metodos de string (`isupper`, `isalnum`, `isascii`, etc.), validacao de formato de texto |
| `Dicionarios e Tuplas/` | 10 | `dict` como estrutura de busca, tuplas como registros imutaveis, grafos simples representados por dicionarios |
| `Listas/` | 10 | Ordenacao, busca, fatiamento, agregacao (soma, media, desvio padrao) sobre listas |
| `Arquivos/` | 10 | Leitura/escrita de arquivos texto e CSV, parsing de linhas delimitadas, processamento de datasets reais |

Os topicos seguem uma progressao didatica: comecam em conceitos isolados (variaveis, condicionais) e terminam em processamento de dados estruturados a partir de arquivos, a mesma progressao reaproveitada nos dois projetos maiores do repositorio irmao.

---

## Requisitos

| Dependencia | Versao | Instalacao |
|---|---|---|
| Python | 3.8+ | `sudo apt install python3` (ou equivalente da distribuicao) |

Nenhuma dependencia externa (`pip`) e necessaria: todos os scripts usam apenas a biblioteca padrao.

---

## Como Executar

Cada exercicio e um script Python independente que le sua entrada via `stdin`, seguindo o formato descrito no respectivo `Enunciado N.PNG`. Exemplo concreto (Listas, Questao 5, media e desvio padrao de uma lista de numeros):

```bash
$ echo "5
1 2 3 4 5" | python3 "Listas/Questão 5/Resposta 5.py"
3.00 1.41
```

Tambem e possivel redirecionar de um arquivo ou digitar interativamente:

```bash
python3 "Variaveis e Expressões/Questão 1/Resposta 1.py" < entrada.txt
python3 "Arquivos/Questão 3/Resposta 3.py"   # pede o nome do arquivo a ler interativamente
```

---

## Exercicios por Topico

| Pasta | Questoes | Bugs encontrados |
|---|---|---|
| Variaveis e Expressões | 10 | 1 |
| Condicionais e Recursividade | 10 | 3 |
| Funções | 10 | 1 |
| Funções com Resultado | 10 | 1 |
| Iterações | 10 | 2 |
| Strings | 10 | 2 |
| Dicionarios e Tuplas | 10 | 3 |
| Listas | 10 | 4 |
| Arquivos | 10 | 4 |
| **Total** | **90** | **21** |

---

> Documentacao gerada com auxilio de IA.
