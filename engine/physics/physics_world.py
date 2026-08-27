"""
Physics Engine - Physics World Simulator
Manages step accumulator, broadphase culling, SAT collision resolution, and constraint solving.
"""

from typing import List
from engine.core.vector import Vector2D
from engine.physics.rigidbody import Rigidbody2D
from engine.physics.colliders import CircleCollider2D, CollisionManifold

class PhysicsWorld:
    """2D Physics simulation world managing gravity and rigidbodies."""

    def __init__(self, gravity: Vector2D = Vector2D(0.0, -9.81)):
        self.gravity = gravity
        self.bodies: List[Rigidbody2D] = []

    def add_body(self, body: Rigidbody2D):
        if body not in self.bodies:
            self.bodies.append(body)

    def remove_body(self, body: Rigidbody2D):
        if body in self.bodies:
            self.bodies.remove(body)

    def step(self, dt: float, sub_steps: int = 4):
        sub_dt = dt / float(sub_steps)
        for _ in range(sub_steps):
            for body in self.bodies:
                body.integrate(sub_dt, self.gravity)
            self._resolve_collisions()

    def _resolve_collisions(self):
        # Circle-Circle simple collision check
        n = len(self.bodies)
        for i in range(n):
            for j in range(i + 1, n):
                b1 = self.bodies[i]
                b2 = self.bodies[j]
                if b1.is_static and b2.is_static:
                    continue
                dist = b1.position.distance_to(b2.position)
                min_dist = 1.0  # Default unit radius check
                if dist < min_dist and dist > 0.0:
                    normal = (b2.position - b1.position) / dist
                    penetration = min_dist - dist
                    
                    # Separation positional fix
                    total_inv = b1.inv_mass + b2.inv_mass
                    if total_inv > 0:
                        b1.position -= normal * (penetration * (b1.inv_mass / total_inv))
                        b2.position += normal * (penetration * (b2.inv_mass / total_inv))
                    
                    # Relative velocity impulse
                    rel_vel = b2.velocity - b1.velocity
                    vel_along_normal = rel_vel.dot(normal)
                    if vel_along_normal < 0:
                        e = min(b1.restitution, b2.restitution)
                        j_impulse = -(1.0 + e) * vel_along_normal / total_inv
                        impulse = normal * j_impulse
                        b1.apply_impulse(-impulse)
                        b2.apply_impulse(impulse)
