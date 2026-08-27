"""
Graphics Engine - Dynamic Lighting & Shadow Mapping
Implements 2D Point Light attenuation, Directional Sunlight calculations, and ambient occlusion overlays.
"""

import math
from typing import List, Tuple
from engine.core.vector import Vector2D
from engine.graphics.render_context import Color

class PointLight2D:
    """2D Point light source with radial distance attenuation."""
    def __init__(self, position: Vector2D, radius: float = 150.0, color: Color = None, intensity: float = 1.0):
        self.position = position
        self.radius = radius
        self.color = color if color else Color(1.0, 0.8, 0.9, 1.0)
        self.intensity = intensity

    def get_attenuation(self, point: Vector2D) -> float:
        dist = self.position.distance_to(point)
        if dist >= self.radius:
            return 0.0
        att = 1.0 - (dist / self.radius)
        return max(0.0, att * att * self.intensity)
