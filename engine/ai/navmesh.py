"""
AI Engine - NavMesh Polygon Graph Pathfinding
Provides convex polygon navigation mesh generation and A* node traversal for complex maps.
"""

from typing import List, Tuple
from engine.core.vector import Vector2D

class NavMeshPoly:
    """Convex polygon in navigation mesh."""
    def __init__(self, vertices: List[Vector2D]):
        self.vertices = vertices
        self.neighbors: List['NavMeshPoly'] = []

    def contains_point(self, pt: Vector2D) -> bool:
        # Cross product point in polygon test
        n = len(self.vertices)
        for i in range(n):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % n]
            edge = p2 - p1
            to_pt = pt - p1
            if edge.cross(to_pt) < 0:
                return False
        return True
