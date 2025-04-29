import unittest
from pathfinder import PathFinder

class TestPathFinder(unittest.TestCase):
    def setUp(self):
        self.maze1 = [
            ['S', '0', '1', '0', '0'],
            ['0', '0', '1', '0', '1'],
            ['0', '1', '0', '0', '0'],
            ['1', '0', '0', 'E', '1']
        ]

        self.maze2 = [
            ['S', '0', '1', '0', '0'],
            ['0', '0', '1', '0', '1'],
            ['0', '1', '0', '0', '0'],
            ['1', '1', '1', 'E', '1']
        ]

    def test_find_path_success(self):
        pathfinder = PathFinder(self.maze1)
        path = pathfinder.find_path()
        self.assertIsNotNone(path)
        self.assertEqual(path[0], (0, 0))  # Início
        self.assertEqual(path[-1], (3, 3))  # Fim

    def test_find_path_no_solution(self):
        pathfinder = PathFinder(self.maze2)
        path = pathfinder.find_path()
        self.assertIsNone(path)

    def test_visualize_path(self):
        pathfinder = PathFinder(self.maze1)
        path = pathfinder.find_path()
        visualization = pathfinder.visualize_path(path)
        
        # Verifica se o caminho está marcado com '*'
        self.assertIn('*', visualization)
        # Verifica se S e E estão presentes
        self.assertIn('S', visualization)
        self.assertIn('E', visualization)

if __name__ == '__main__':
    unittest.main() 