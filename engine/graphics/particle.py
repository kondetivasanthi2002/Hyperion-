"""
Graphics Engine - Particle System
Handles particle emission, physics integration, color curves, and particle rendering.
"""

import random
from typing import List
from engine.core.vector import Vector2D
from engine.graphics.render_context import Color, RenderContext

class Particle:
    """Individual particle instance."""
    __slots__ = ('position', 'velocity', 'color', 'start_color', 'end_color', 'size', 'start_size', 'end_size', 'life', 'max_life')

    def __init__(self, position: Vector2D, velocity: Vector2D, color: Color, size: float, max_life: float):
        self.position = position
        self.velocity = velocity
        self.color = color
        self.start_color = color
        self.end_color = Color(color.r, color.g, color.b, 0.0)
        self.size = size
        self.start_size = size
        self.end_size = 0.0
        self.life = max_life
        self.max_life = max_life

    def update(self, dt: float) -> bool:
        self.life -= dt
        if self.life <= 0.0:
            return False
        
        t = 1.0 - (self.life / self.max_life)
        self.position += self.velocity * dt
        self.size = self.start_size + (self.end_size - self.start_size) * t
        
        # Color lerp
        self.color = Color(
            self.start_color.r + (self.end_color.r - self.start_color.r) * t,
            self.start_color.g + (self.end_color.g - self.start_color.g) * t,
            self.start_color.b + (self.end_color.b - self.start_color.b) * t,
            self.start_color.a + (self.end_color.a - self.start_color.a) * t
        )
        return True


class ParticleEmitter:
    """Particle emitter managing burst rates and particle pools."""

    def __init__(self, position: Vector2D = None):
        self.position = position if position else Vector2D.zero()
        self.particles: List[Particle] = []
        self.emission_rate = 50.0  # Particles per second
        self.accumulator = 0.0

    def emit_burst(self, count: int, speed: float = 100.0):
        for _ in range(count):
            angle = random.uniform(0.0, 6.28318)
            vel = Vector2D(math.cos(angle), math.sin(angle)) * random.uniform(speed * 0.5, speed)
            p = Particle(
                position=Vector2D(self.position.x, self.position.y),
                velocity=vel,
                color=Color.red(),
                size=5.0,
                max_life=random.uniform(0.5, 1.5)
            )
            self.particles.append(p)

    def update(self, dt: float):
        self.particles = [p for p in self.particles if p.update(dt)]
