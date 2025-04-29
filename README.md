# PathFinder - Resolvendo o Labirinto 2D com o Algoritmo A\*

Este projeto implementa o algoritmo A\* para encontrar o menor caminho em um labirinto 2D entre um ponto inicial (S) e um ponto final (E), evitando obstáculos.

## Descrição do Problema

O problema consiste em encontrar o caminho mais curto em um labirinto 2D, onde:

- 'S' representa o ponto inicial
- 'E' representa o ponto final
- '0' representa células livres
- '1' representa obstáculos

O robô pode se mover apenas nas direções cardeais (cima, baixo, esquerda, direita) e cada movimento tem custo 1.

## Algoritmo A\*

O algoritmo A\* é um algoritmo de busca informada que combina:

- g(n): Custo real do caminho do início até o nó atual
- h(n): Heurística (estimativa) do custo do nó atual até o objetivo

A função de avaliação f(n) = g(n) + h(n) é usada para determinar qual nó explorar primeiro.

### Heurística

Utilizamos a distância de Manhattan como heurística:

```
h(n) = |x_atual - x_final| + |y_atual - y_final|
```

## Requisitos

- Python 3.7+
- NumPy

## Instalação

1. Clone o repositório:

```bash
git clone [URL_DO_REPOSITÓRIO]
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

Execute o programa:

```bash
python pathfinder.py
```

O programa irá:

1. Carregar o labirinto de exemplo
2. Encontrar o caminho mais curto usando A\*
3. Exibir o caminho em coordenadas
4. Mostrar o labirinto com o caminho destacado

## Exemplo de Saída

Para o labirinto:

```
S 0 1 0 0
0 0 1 0 1
0 1 0 0 0
1 0 0 E 1
```

A saída será:

```
Menor caminho (em coordenadas):
[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]

Labirinto com o caminho destacado:
S 0 1 0 0
* * 1 0 1
1 * 1 0 0
1 * * E 1
```

## Estrutura do Código

- `Node`: Classe que representa um nó no labirinto
- `PathFinder`: Classe principal que implementa o algoritmo A\*
- Funções auxiliares para manipulação do labirinto e visualização
# pathfinder
