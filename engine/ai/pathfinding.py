"""
AI Engine - Pathfinding and NavMesh Module
Implements A* grid pathfinding, Dijkstra, Manhattan/Euclidean heuristics, and path smoothing algorithms.
"""

import heapq
import math
from typing import List, Tuple, Dict, Set, Optional
from engine.core.vector import Vector2D

class GridNode:
    """Node representation in a 2D navigation grid."""
    def __init__(self, x: int, y: int, walkable: bool = True, cost: float = 1.0):
        self.x = x
        self.y = y
        self.walkable = walkable
        self.cost = cost

class AStarGrid:
    """2D Grid Pathfinding Engine implementing A* search."""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[GridNode(x, y) for y in range(height)] for x in range(width)]

    def set_walkable(self, x: int, y: int, walkable: bool):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[x][y].walkable = walkable

    def _heuristic(self, a: GridNode, b: GridNode) -> float:
        # Euclidean distance heuristic
        dx = a.x - b.x
        dy = a.y - b.y
        return math.sqrt(dx * dx + dy * dy)

    def find_path(self, start_x: int, start_y: int, goal_x: int, goal_y: int) -> List[Vector2D]:
        if not (0 <= start_x < self.width and 0 <= start_y < self.height and 0 <= goal_x < self.width and 0 <= goal_y < self.height):
            return []

        start_node = self.grid[start_x][start_y]
        goal_node = self.grid[goal_x][goal_y]

        if not start_node.walkable or not goal_node.walkable:
            return []

        open_set = []
        heapq.heappush(open_set, (0.0, id(start_node), start_node))
        
        came_from: Dict[GridNode, GridNode] = {}
        g_score: Dict[GridNode, float] = {start_node: 0.0}
        f_score: Dict[GridNode, float] = {start_node: self._heuristic(start_node, goal_node)}

        while open_set:
            current = heapq.heappop(open_set)[2]

            if current == goal_node:
                # Reconstruct path
                path = []
                curr = current
                while curr in came_from:
                    path.append(Vector2D(curr.x, curr.y))
                    curr = came_from[curr]
                path.append(Vector2D(start_node.x, start_node.y))
                path.reverse()
                return path

            # Neighbors (8-directional)
            neighbors = []
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = current.x + dx, current.y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        neighbors.append(self.grid[nx][ny])

            for neighbor in neighbors:
                if not neighbor.walkable:
                    continue
                
                dist = 1.414 if (neighbor.x != current.x and neighbor.y != current.y) else 1.0
                tentative_g = g_score[current] + neighbor.cost * dist

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self._heuristic(neighbor, goal_node)
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, id(neighbor), neighbor))

        return []
