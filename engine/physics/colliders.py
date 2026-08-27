"""
Physics Engine - Colliders and Shape Definitions
Defines BoxCollider2D, CircleCollider2D, PolygonCollider2D, and collision manifolds.
"""

from typing import List, Tuple
from engine.core.vector import Vector2D

class CollisionManifold:
    """Stores contact information between two colliding bodies."""

    def __init__(self, body_a=None, body_b=None):
        self.body_a = body_a
        self.body_b = body_b
        self.normal = Vector2D(0.0, 1.0)
        self.penetration = 0.0
        self.contacts: List[Vector2D] = []
        self.collided = False

class BoxCollider2D:
    """Axis-Aligned or Oriented Bounding Box Collider."""

    def __init__(self, width: float = 1.0, height: float = 1.0, offset: Vector2D = None):
        self.width = float(width)
        self.height = float(height)
        self.offset = offset if offset else Vector2D(0.0, 0.0)

    def get_vertices(self, position: Vector2D, rotation: float) -> List[Vector2D]:
        hw = self.width * 0.5
        hh = self.height * 0.5
        local_verts = [
            Vector2D(-hw, -hh),
            Vector2D(hw, -hh),
            Vector2D(hw, hh),
            Vector2D(-hw, hh)
        ]
        world_verts = []
        for v in local_verts:
            rotated = (v + self.offset).rotate(rotation)
            world_verts.append(rotated + position)
        return world_verts

class CircleCollider2D:
    """Bounding Circle Collider."""

    def __init__(self, radius: float = 0.5, offset: Vector2D = None):
        self.radius = float(radius)
        self.offset = offset if offset else Vector2D(0.0, 0.0)
