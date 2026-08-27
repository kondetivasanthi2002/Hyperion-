"""Automated Test Suite 4: AI & Pathfinding Tests"""
import unittest
from engine.ai.pathfinding import AStarGrid

class TestAIPathfinding(unittest.TestCase):
    def test_astar_grid_path(self):
        grid = AStarGrid(10, 10)
        path = grid.find_path(0, 0, 5, 5)
        self.assertTrue(len(path) > 0)
        self.assertEqual(path[0].x, 0)
        self.assertEqual(path[0].y, 0)

if __name__ == '__main__':
    unittest.main()
