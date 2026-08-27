"""
Physics Engine - Rigidbody Dynamics Module
Implements 2D/3D rigidbody physics state, velocity integration, force/torque accumulators, and damping models.
"""

import math
from engine.core.vector import Vector2D, Vector3D

class Rigidbody2D:
    """2D Rigidbody handling translational and rotational dynamics."""

    def __init__(self, mass: float = 1.0, is_static: bool = False):
        self.mass = mass if not is_static else 0.0
        self.inv_mass = 1.0 / mass if mass > 0 and not is_static else 0.0
        self.inertia = 10.0 if not is_static else 0.0
        self.inv_inertia = 1.0 / self.inertia if self.inertia > 0 and not is_static else 0.0
        self.is_static = is_static
        
        self.position = Vector2D(0.0, 0.0)
        self.velocity = Vector2D(0.0, 0.0)
        self.force_accumulator = Vector2D(0.0, 0.0)
        
        self.rotation = 0.0  # Radians
        self.angular_velocity = 0.0
        self.torque_accumulator = 0.0
        
        self.linear_damping = 0.01
        self.angular_damping = 0.05
        self.restitution = 0.5  # Bounciness
        self.friction = 0.3     # Surface friction

    def apply_force(self, force: Vector2D):
        if not self.is_static:
            self.force_accumulator += force

    def apply_impulse(self, impulse: Vector2D, contact_point: Vector2D = None):
        if not self.is_static:
            self.velocity += impulse * self.inv_mass
            if contact_point:
                r = contact_point - self.position
                self.angular_velocity += r.cross(impulse) * self.inv_inertia

    def integrate(self, dt: float, gravity: Vector2D = Vector2D(0.0, -9.81)):
        if self.is_static:
            return
        
        # Apply gravity
        self.force_accumulator += gravity * self.mass
        
        # Integrate linear motion
        acceleration = self.force_accumulator * self.inv_mass
        self.velocity += acceleration * dt
        self.velocity *= max(0.0, 1.0 - self.linear_damping * dt)
        self.position += self.velocity * dt
        
        # Integrate rotational motion
        angular_acceleration = self.torque_accumulator * self.inv_inertia
        self.angular_velocity += angular_acceleration * dt
        self.angular_velocity *= max(0.0, 1.0 - self.angular_damping * dt)
        self.rotation += self.angular_velocity * dt
        
        # Clear accumulators
        self.force_accumulator = Vector2D(0.0, 0.0)
        self.torque_accumulator = 0.0
