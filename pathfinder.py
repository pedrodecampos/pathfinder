import numpy as np
from typing import List, Tuple, Optional
import heapq

class Node:
    def __init__(self, position: Tuple[int, int], parent: Optional['Node'] = None):
        self.position = position
        self.parent = parent
        self.g = 0  # Custo do caminho do início até este nó
        self.h = 0  # Heurística (distância estimada até o objetivo)
        self.f = 0  # Custo total (g + h)

    def __lt__(self, other):
        return self.f < other.f

class PathFinder:
    def __init__(self, maze: List[List[str]]):
        self.maze = np.array(maze)
        self.start = self._find_position('S')
        self.end = self._find_position('E')
        self.rows, self.cols = self.maze.shape

    def _find_position(self, target: str) -> Tuple[int, int]:
        positions = np.where(self.maze == target)
        if len(positions[0]) == 0:
            raise ValueError(f"Posição {target} não encontrada no labirinto")
        return (positions[0][0], positions[1][0])

    def _is_valid_position(self, pos: Tuple[int, int]) -> bool:
        row, col = pos
        return (0 <= row < self.rows and 
                0 <= col < self.cols and 
                self.maze[row, col] != '1')

    def _get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        row, col = pos
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # direita, baixo, esquerda, cima
        neighbors = []
        
        for dr, dc in directions:
            new_pos = (row + dr, col + dc)
            if self._is_valid_position(new_pos):
                neighbors.append(new_pos)
        
        return neighbors

    def _manhattan_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def find_path(self) -> Optional[List[Tuple[int, int]]]:
        if not self.start or not self.end:
            return None

        open_list = []
        closed_set = set()

        start_node = Node(self.start)
        start_node.g = 0
        start_node.h = self._manhattan_distance(self.start, self.end)
        start_node.f = start_node.g + start_node.h

        heapq.heappush(open_list, (start_node.f, start_node))

        while open_list:
            current_f, current_node = heapq.heappop(open_list)
            current_pos = current_node.position

            if current_pos == self.end:
                path = []
                while current_node:
                    path.append(current_node.position)
                    current_node = current_node.parent
                return path[::-1]

            closed_set.add(current_pos)

            for neighbor_pos in self._get_neighbors(current_pos):
                if neighbor_pos in closed_set:
                    continue

                neighbor_node = Node(neighbor_pos, current_node)
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = self._manhattan_distance(neighbor_pos, self.end)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                # Verifica se o vizinho já está na lista aberta com um custo menor
                found = False
                for i, (f, node) in enumerate(open_list):
                    if node.position == neighbor_pos and f <= neighbor_node.f:
                        found = True
                        break

                if not found:
                    heapq.heappush(open_list, (neighbor_node.f, neighbor_node))

        return None

    def visualize_path(self, path: List[Tuple[int, int]]) -> str:
        if not path:
            return "Sem solução"

        visualization = self.maze.copy()
        for pos in path[1:-1]:  # Exclui o início e o fim
            visualization[pos] = '*'

        return '\n'.join([' '.join(row) for row in visualization])

def main():
    # Exemplo de uso
    maze = [
        ['S', '0', '1', '0', '0'],
        ['0', '0', '1', '0', '1'],
        ['0', '1', '0', '0', '0'],
        ['1', '0', '0', 'E', '1']
    ]

    pathfinder = PathFinder(maze)
    path = pathfinder.find_path()

    if path:
        print("Menor caminho (em coordenadas):")
        print(path)
        print("\nLabirinto com o caminho destacado:")
        print(pathfinder.visualize_path(path))
    else:
        print("Sem solução")

if __name__ == "__main__":
    main() 