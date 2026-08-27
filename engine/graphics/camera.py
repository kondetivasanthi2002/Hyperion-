"""
Graphics Engine - Camera Controllers
Manages Camera2D and Camera3D transforms, smooth target tracking, zoom lerp, and screen-to-world projections.
"""

import math
from engine.core.vector import Vector2D
from engine.core.matrix import Matrix4x4

class Camera2D:
    """2D Viewport Camera supporting smooth pan, zoom, and screen shake."""

    def __init__(self, viewport_width: float = 800.0, viewport_height: float = 600.0):
        self.position = Vector2D(0.0, 0.0)
        self.target_position = Vector2D(0.0, 0.0)
        self.zoom = 1.0
        self.target_zoom = 1.0
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        self.smoothing = 5.0  # Lerp speed
        self.shake_intensity = 0.0

    def update(self, dt: float):
        # Smooth camera movement
        self.position = self.position.lerp(self.target_position, max(0.0, min(1.0, dt * self.smoothing)))
        self.zoom += (self.target_zoom - self.zoom) * max(0.0, min(1.0, dt * self.smoothing))
        
        # Shake decay
        if self.shake_intensity > 0.0:
            self.shake_intensity = max(0.0, self.shake_intensity - dt * 10.0)

    def add_shake(self, intensity: float):
        self.shake_intensity = max(self.shake_intensity, intensity)

    def world_to_screen(self, world_pos: Vector2D) -> Vector2D:
        rel = (world_pos - self.position) * self.zoom
        return Vector2D(
            rel.x + self.viewport_width * 0.5,
            self.viewport_height * 0.5 - rel.y
        )

    def screen_to_world(self, screen_pos: Vector2D) -> Vector2D:
        rel_x = (screen_pos.x - self.viewport_width * 0.5) / self.zoom
        rel_y = (self.viewport_height * 0.5 - screen_pos.y) / self.zoom
        return Vector2D(rel_x, rel_y) + self.position
